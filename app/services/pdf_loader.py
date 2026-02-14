from pypdf import PdfReader
CHUNK_SIZE = 1024

def load_pdf(file_path: str) -> str:
    """
    Reads a PDF and returns full extracted text.
    """
    reader = PdfReader(file_path)
    text = ""

    for page in reader.pages:
        extracted = page.extract_text()
        if extracted:
            text += extracted + "\n"

    return text

def split_text(text: str, chunk_size: int = CHUNK_SIZE):
    """
    Splits text into fixed-size chunks.
    """
    chunks = []

    for i in range(0, len(text), chunk_size):
        chunk = text[i:i + chunk_size]
        chunks.append(chunk)

    return chunks


def load_and_split_pdf(file_path: str):
    """
    Main function used by API.
    """
    text = load_pdf(file_path)
    chunks = split_text(text)
    return chunks