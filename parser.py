import os
import fitz  # PyMuPDF for PDF parsing
from concurrent.futures import ThreadPoolExecutor

# Extract text from a PDF
def extract_text_from_pdf(file_path):
    pdf_text = ""
    try:
        with fitz.open(file_path) as pdf_document:
            for page_num in range(pdf_document.page_count):
                page = pdf_document[page_num]
                pdf_text += page.get_text("text")
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
    return pdf_text

# Classify PDF by page count
def classify_pdf(file_path):
    try:
        with fitz.open(file_path) as pdf_document:
            num_pages = pdf_document.page_count
            size = 'short' if num_pages <= 10 else 'medium' if num_pages <= 30 else 'long'
            print(f"{file_path} classified as {size} with {num_pages} pages.")
            return {'file': file_path, 'size': size, 'pages': num_pages}
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return None

# Process multiple PDFs concurrently
def process_pdfs(directory):
    pdf_files = [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith('.pdf')]
    with ThreadPoolExecutor() as executor:
        results = list(executor.map(classify_pdf, pdf_files))
    return [result for result in results if result]
