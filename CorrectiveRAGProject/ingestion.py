from pathlib import Path
from dotenv import load_dotenv
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings

# .env dosyasını bu script'in bulunduğu klasörden yükle (çalışma dizininden bağımsız)
load_dotenv(Path(__file__).resolve().parent / ".env")

# Uyarıları azalt: WebBaseLoader USER_AGENT ister; Chroma telemetry hatası önlenir
import os
if not os.environ.get("USER_AGENT"):
    os.environ["USER_AGENT"] = "CorrectiveRAG/1.0"
os.environ["ANONYMIZED_TELEMETRY"] = "FALSE"

urls =["https://lilianweng.github.io/posts/2023-06-23-agent/",
       "https://lilianweng.github.io/posts/2023-03-15-prompt-engineering/",
       "https://lilianweng.github.io/posts/2023-10-25-adv-attack-llm/"
       ]

docs = [WebBaseLoader(url).load() for url in urls]
docs_list= [item for sublist in docs for item in sublist]

text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
    chunk_size =250, chunk_overlap=0)

splits=text_splitter.split_documents(docs_list)

vectorstore =Chroma.from_documents(
    documents=splits,
    collection_name="rag-chroma",
    embedding=OpenAIEmbeddings(),
    persist_directory="./.chroma"
)

retriever= Chroma(
    collection_name="rag-chroma",
    persist_directory="./.chroma",
    embedding_function=OpenAIEmbeddings(),
).as_retriever()

if __name__ == "__main__":
    print("Ingestion tamamlandi.")
    print(f"  - {len(docs_list)} belge yuklendi, {len(splits)} chunk olusturuldu.")
    print("  - Vectorstore .chroma klasorune kaydedildi.")