from dotenv import load_dotenv
load_dotenv()

from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

PERSIST_DIRECTORY = "app/db/chroma_db"


def get_vector_store():
    embeddings = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2"
    )

    vector_store = Chroma(
        persist_directory=PERSIST_DIRECTORY,
        embedding_function=embeddings
    )

    return vector_store


def store_chunks(chunks):
    vector_store = get_vector_store()

    vector_store.add_texts(chunks)
    vector_store.persist()

    return len(chunks)
