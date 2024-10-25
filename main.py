import os
import json
from datetime import datetime
from parser import process_pdfs, extract_text_from_pdf
from connection import get_mongo_client, store_or_update_metadata
from summarizer import summarize_text, extract_keywords

def process_and_store_pdf(file_data, client, output_messages):
    file_path = file_data['file']
    size = file_data['size']
    num_pages = file_data['pages']
    
    pdf_text = extract_text_from_pdf(file_path)

    summary = summarize_text(pdf_text)
    keywords = extract_keywords(pdf_text)

    # Store or update the PDF metadata in MongoDB
    updated_message = store_or_update_metadata(client, file_path, size, num_pages, summary, keywords)
    
    # Collect the output message
    output_messages.append(updated_message)

def save_output_to_json(output_messages):
    # Create Output directory if it doesn't exist
    output_dir = os.path.join(os.getcwd(), 'Output')
    os.makedirs(output_dir, exist_ok=True)
    
    # Generate timestamped filename
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = os.path.join(output_dir, f"{timestamp}.json")

    # Write output messages to JSON file
    with open(output_file, 'w') as json_file:
        json.dump(output_messages, json_file, indent=4)

    print(f"Output saved to {output_file}")

if __name__ == "__main__":
    directory = os.path.expanduser("~/Desktop/pdf_dataset/")  # Path to PDF directory
    client = get_mongo_client()  # MongoDB connection

    # List to hold all output messages
    output_messages = []

    # Process PDFs and store metadata in MongoDB
    pdfs = process_pdfs(directory)
    for pdf_data in pdfs:
        process_and_store_pdf(pdf_data, client, output_messages)

    # Save all output messages to JSON file
    save_output_to_json(output_messages)
