from ingestion import retriever
from graph.state import GraphState
from typing import Dict,Any

def retrieve(state: GraphState) -> Dict[str, Any]:

    print("----RETRİEVE----")

    question=state["question"]
    documents = retriever.invoke(question)
    return {"question":question,"documents":documents}