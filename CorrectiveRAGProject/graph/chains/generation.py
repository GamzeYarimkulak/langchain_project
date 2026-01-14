from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

llm=ChatOpenAI(temperature=0)
prompt = ChatPromptTemplate.from_messages([
    ("system",
     "You are a RAG assistant. Use ONLY the provided context to answer.\n"
     "If the answer is not in the context, say: 'Bunu verilen kaynaklardan doğrulayamıyorum.'\n"
     "Keep the answer concise and factual."),
    ("human", "Question: {question}\n\nContext:\n{context}\n\nAnswer:")
])

generation_chain= prompt | llm | StrOutputParser()