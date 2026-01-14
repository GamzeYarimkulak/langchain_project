from dotenv import load_dotenv
from langgraph.graph import END, StateGraph

from graph.node_constants import RETRIEVE, GENERATE, WEBSEARCH, GRADE_DOCUMENTS
from graph.nodes import generate, grade_documents, web_search, retrieve
from graph.state import GraphState

from graph.chains.router import question_router
from graph.chains.hallucination_grader import hallucination_grader
from graph.chains.answer_grader import answer_grader

load_dotenv()


def route_question(state: GraphState) -> str:
    """Route question either to websearch or vectorstore retrieval."""
    print("ROUTE QUESTION")
    question = state["question"]

    source = question_router.invoke({"question": question})

    if getattr(source, "datasource", None) == "websearch":
        print("WEBSEARCH")
        return WEBSEARCH

    if getattr(source, "datasource", None) == "vectorstore":
        print("VECTORSTORE")
        return RETRIEVE

    # Safe fallback
    print("ROUTER FALLBACK -> WEBSEARCH")
    return WEBSEARCH


def decide_to_generate(state: GraphState) -> str:
    """After grading retrieved docs, decide to do web search or generate."""
    print("--- ASSESS GRADED DOCUMENTS ---")
    if state.get("web_search", False):
        print("WEB_SEARCH")
        return WEBSEARCH
    return GENERATE


def grade_generation_grounded_in_documents_and_question(state: GraphState) -> str:
    print("CHECK HALLUCINATION / ANSWER QUALITY")
    print("ATTEMPTS =", state.get("attempts", 0))

    attempts = state.get("attempts", 0)
    if attempts >= 3:
        print("STOPPING AFTER 3 ATTEMPTS")
        return "useful"  # veya "not useful" deyip END'e bağlayabilirsin

    question = state["question"]
    documents = state.get("documents", [])
    generation = state["generation"]

    h_score = hallucination_grader.invoke({"documents": documents, "generation": generation})
    grounded = str(getattr(h_score, "binary_score", "")).lower() == "yes"

    if not grounded:
        print("GENERATION IS NOT GROUNDED IN DOCUMENTS")
        return "not supported"

    print("GENERATION IS GROUNDED IN DOCUMENTS")

    a_score = answer_grader.invoke({"question": question, "documents": documents, "generation": generation})
    answers_question = str(a_score.binary_score).lower() == "yes"


    if answers_question:
        print("GENERATION ADDRESSES QUESTION")
        return "useful"

    print("GENERATION DOES NOT ADDRESS QUESTION")
    return "not useful"




# --- Build graph ---
workflow = StateGraph(GraphState)

# Nodes
workflow.add_node(RETRIEVE, retrieve)
workflow.add_node(GRADE_DOCUMENTS, grade_documents)
workflow.add_node(WEBSEARCH, web_search)
workflow.add_node(GENERATE, generate)

# Entry routing
workflow.set_conditional_entry_point(
    route_question,
    {
        WEBSEARCH: WEBSEARCH,
        RETRIEVE: RETRIEVE,
    },
)


# Retrieval branch: retrieve -> grade docs -> (websearch or generate)
workflow.add_edge(RETRIEVE, GRADE_DOCUMENTS)
workflow.add_conditional_edges(
    GRADE_DOCUMENTS,
    decide_to_generate,
    {
        WEBSEARCH: WEBSEARCH,
        GENERATE: GENERATE,
    },
)

# Websearch branch: websearch -> generate
workflow.add_edge(WEBSEARCH, GENERATE)

# After generate: decide end / websearch / etc.
# NOTE: "not supported" is usually better routed to WEBSEARCH (or RETRIEVE),
# otherwise you can loop on GENERATE forever.
workflow.add_conditional_edges(
    GENERATE,
    grade_generation_grounded_in_documents_and_question,
    {
        "useful": END,
        "not useful": WEBSEARCH,
        "not supported": WEBSEARCH,
    },
)

app = workflow.compile()

# Optional: draw graph (requires mermaid support in your env)
try:
    app.get_graph().draw_mermaid_png(output_file_path="graph.png")
except Exception as e:
    print(f"Graph draw skipped: {e}")




