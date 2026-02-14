from app.services.pdf_loader import load_and_split_pdf

chunks = load_and_split_pdf("Updated_Resume.pdf")

print(len(chunks))
print(chunks[0])
