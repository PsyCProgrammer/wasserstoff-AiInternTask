# PDF Pipeline Project

This project automates the process of reading PDF files, classifying them by length, summarizing their content, extracting keywords, and storing metadata in MongoDB. It is built to handle multiple PDFs efficiently using concurrent processing. Upon execution it saves the log file as json in Output folder in the same directory.

## Features

- Extract text and classify PDFs by page count (short, medium, long).
- Generate summaries and keywords for each PDF.
- Store metadata, summaries, and keywords in MongoDB.

## Project Structure

- `main.py`: Main script to process PDFs and store metadata.
- `parser.py`: Contains functions to classify PDFs, extract text, summarize, and extract keywords.
- `connection.py`: Handles MongoDB connection and metadata storage.
- `semmarizer.py`: Extract frequent words and summerizes the pdf.

## Prerequisites

- **Python 3.11+**
- **MongoDB** installed and running locally or on a remote server.

## Setup

1. **Clone this repository** and navigate to the project directory.

    ```bash
    git clone <repository_url>
    cd pdf_project
    ```

2. **Create and activate a virtual environment**:

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Download NLTK Data**:
   
   Ensure that necessary NLTK datasets, such as `punkt` and `stopwords`, are downloaded.

    ```python
    import nltk
    nltk.download('punkt')
    nltk.download('stopwords')
    ```

## Usage

1. **Prepare PDFs**: Place the PDF files you want to process in a directory (e.g., `~/Desktop/pdf_dataset`).

2. **Run the Project**:

    Run the main script to process the PDFs, summarize content, extract keywords, and store metadata in MongoDB.

    ```bash
    python main.py
    ```

3. **Check MongoDB for Stored Data**:
   
   Connect to your MongoDB instance and inspect the `pdf_pipeline` database and `pdf_metadata` collection to see the stored metadata, summaries, and keywords.

## Troubleshooting

- **ModuleNotFoundError**: Ensure all packages are installed by running `pip install -r requirements.txt`.
- **MongoDB Connection Issues**: Verify that MongoDB is running on `localhost:27017` or update the MongoDB URI in `db_connection.py`.

## License

This project is licensed under the MIT License.
