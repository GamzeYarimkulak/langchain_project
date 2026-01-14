from typing import Literal
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.pydantic_v1 import BaseModel, Field

llm =ChatOpenAI(temperature=0)


class GradeHallucination(BaseModel):
    binary_score: Literal["yes", "no"] =Field(
        description ="Answer is grounded in the facts,'yes' or 'no'",
    )


structured_llm_grader= llm.with_structured_output(GradeHallucination)

system_prompts="""
You are a grader assessing whether an LLM generation is grounded in /supported by a set of retrieved facts.
Give a binary score 'yes' or 'no'. 'Yes' means that the answer is grounded in / supported by the set of facts.
"""

hallucination_prompts= ChatPromptTemplate(
    [
        ("system", system_prompts),
        ("human","Set of facts:  \n\n {documents} \n\n LLM generation: {generation}")
    ]
)

hallucination_grader =hallucination_prompts  | structured_llm_grader