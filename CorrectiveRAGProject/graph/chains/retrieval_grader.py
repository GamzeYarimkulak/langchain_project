from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.pydantic_v1 import BaseModel, Field

from ingestion import retriever

load_dotenv()

llm = ChatOpenAI(temperature=0)

class GradeDocuments(BaseModel):
    """Binary score for relevance check on retrieved documents."""
    binary_score: str = Field(description="Documents are relevant to the question: 'yes' or 'no'")

structured_llm_grader = llm.with_structured_output(GradeDocuments)

system_prompt = """
You are a grader assessing whether a retrieved document is relevant to a user question.
Answer with only 'yes' or 'no'.
"""

grade_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "Retrieved document:\n{document}\n\nUser question:\n{question}")
    ]
)

retrieval_grader = grade_prompt | structured_llm_grader

