from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

PERSIST_DIRECTORY = "app/db/chroma_db"


def get_vector_store():
    embeddings = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2"
    )

    return Chroma(
        persist_directory=PERSIST_DIRECTORY,
        embedding_function=embeddings
    )


def ask_question(query: str):
    vector_store = get_vector_store()

    # retrieve top 3 relevant chunks
    docs = vector_store.similarity_search(query, k=3)

    context = "\n\n".join([doc.page_content for doc in docs])

    # simple answer generation (temporary)
    answer = f"""
Answer based on document:

{context}
"""

    return answer
