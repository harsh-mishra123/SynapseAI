from app.services.pdf_loader import load_and_split_pdf
from app.services.vector_store import store_chunks

chunks = load_and_split_pdf("Updated_Resume.pdf")

count = store_chunks(chunks)

print(f"Stored {count} chunks")
