from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_ollama import OllamaLLM

PERSIST_DIRECTORY = "app/db/chroma_db"


def get_vector_store():
    embeddings = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2"
    )

    return Chroma(
        persist_directory=PERSIST_DIRECTORY,
        embedding_function=embeddings
    )


llm = OllamaLLM(model="mistral")


def ask_question(query: str):
    vector_store = get_vector_store()

    docs = vector_store.similarity_search(query, k=3)

    context = "\n\n".join([doc.page_content for doc in docs])

    prompt = f"""
You are a research assistant.
Answer ONLY from the provided context.
If the answer is not in the context, say "Information not found in document."

Context:
{context}

Question:
{query}

Answer:
"""

    response = llm.invoke(prompt)

    return response
