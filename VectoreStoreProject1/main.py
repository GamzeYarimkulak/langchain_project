import os
os.environ["LANGCHAIN_TRACING_V2"] = "false"

from dotenv import load_dotenv
load_dotenv()

from langchain_core.documents import Document
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
from langchain_core.runnables import RunnableLambda,RunnablePassthrough
from langchain_core.prompts import ChatPromptTemplate


documents = [
    Document(page_content="Dogs are great companions, known for their loyalty and friendliness."),
    Document(page_content="Cats are independent pets that often enjoy their own space."),
    Document(page_content="Goldfish are popular pets for beginners."),
    Document(page_content="Parrots are intelligent birds capable of mimicking human speech."),
    Document(page_content="Rabbits are social animals."),
]

embedding = OpenAIEmbeddings(model="text-embedding-3-small")

vectorstore = Chroma.from_documents(
    documents=documents,
    embedding=embedding,
    persist_directory="chroma_store"
)

retriever= RunnableLambda(vectorstore.similarity_search).bind(k=1)

llm =ChatOpenAI(model="gpt-3.5-turbo")

message ="""""

Answer this question using the provided context only.
{question}

Context:

{context}
"""
prompt=ChatPromptTemplate.from_messages([("human",message)])

chain = {"context" : retriever, "question" : RunnablePassthrough()} | prompt |llm


if __name__ == "__main__":
    response =chain.invoke("tell me about dog")
    print(response.content)