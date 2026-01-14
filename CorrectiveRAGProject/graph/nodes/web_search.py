from typing import Any, Dict
from graph.state import GraphState
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.documents import Document

web_search_tool = TavilySearchResults(k=3)

def web_search(state: GraphState) -> Dict[str, Any]:
    print("---WEB SEARCH---")

    question = state["question"]
    documents = state.get("documents") or []

    docs = web_search_tool.invoke({"query": question})

    # Tavily bazen List[str], bazen List[dict] döndürebiliyor.
    if isinstance(docs, list) and docs and isinstance(docs[0], dict):
        web_text = "\n".join([d.get("content", "") for d in docs])
        meta = {"source": "tavily", "type": "dict_results"}
    elif isinstance(docs, list):
        web_text = "\n".join([str(d) for d in docs])
        meta = {"source": "tavily", "type": "string_results"}
    else:
        web_text = str(docs)
        meta = {"source": "tavily", "type": "unknown"}

    documents.append(Document(page_content=web_text, metadata=meta))

    attempts = (state.get("attempts") or 0) + 1
    return {"documents": documents, "question": question, "attempts": attempts}

