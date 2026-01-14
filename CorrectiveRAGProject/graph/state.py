from typing import List,TypedDict

class GraphState(TypedDict):
    """
    Represents the state of a graph.
    Attributes:
        question:question
        generation:LLM generation
        web_search:whether to add search or not
        documents:documents
    """
    question: str
    generation: str
    web_search: bool
    documents: List[str]
    attempts: int