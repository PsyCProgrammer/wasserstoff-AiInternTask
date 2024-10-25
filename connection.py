from pymongo import MongoClient

def get_mongo_client():
    # Establish a connection to MongoDB
    client = MongoClient("mongodb://localhost:27017/")
    return client

def store_or_update_metadata(client, file_name, size, num_pages, summary, keywords):
    # Check if the document already exists
    db = client['pdf_pipeline']
    collection = db['pdf_metadata']

    pdf_metadata = {
        'file': file_name,
        'size': size,
        'pages': num_pages,
        'summary': summary,
        'keywords': keywords
    }

    if collection.find_one({'file': file_name}):
        # If it exists, update the existing document
        collection.update_one(
            {'file': file_name},
            {'$set': pdf_metadata}
        )
        return f"Updated {file_name} with summary and keywords."
    else:
        # If it doesn't exist, create a new entry
        collection.insert_one(pdf_metadata)
        return f"Stored metadata for {file_name}."

