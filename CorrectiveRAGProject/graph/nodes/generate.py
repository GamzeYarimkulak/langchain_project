from graph.chains.generation import generation_chain
from graph.state import GraphState
from typing import Any, Dict

def generate(state: GraphState) -> Dict[str, Any]:
    print("---GENERATE----")
    question = state["question"]
    documents = state.get("documents") or []

    context = "\n\n".join([d.page_content for d in documents])

    generation = generation_chain.invoke(
        {"context": context, "question": question}
    )
    attempts = state.get("attempts", 0)
    return {"question": question, "documents": documents, "generation": generation, "attempts": attempts}

