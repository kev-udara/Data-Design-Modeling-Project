from pymongo import MongoClient
import sys
import json

def load_config():
    with open("config.json", "r") as f:
        return json.load(f)

def load_data_from_mongodb(collection):
    # Retrieve all documents from the collection
    return list(collection.find({}))

def dataset_size(data, collection_name, output_file):
    with open(output_file, 'a', encoding='utf-8') as f:
        f.write(f"Analyzing collection: {collection_name}\n")
        total_records = len(data)
        f.write(f"Total number of records: {total_records}\n")
        
        # Calculate size in memory
        size_in_bytes = sys.getsizeof(data)
        size_in_mb = size_in_bytes / (1024 * 1024)
        f.write(f"Size of dataset in memory: {size_in_mb:.2f} MB\n")
        
        # Size of individual items
        sizes = [sys.getsizeof(item) for item in data]
        avg_size = sum(sizes) / len(sizes)
        f.write(f"Average size of each record: {avg_size:.2f} bytes\n")
        
        # Optionally, list sizes of specific fields
        field_sizes = {}
        for item in data:
            for key, value in item.items():
                field_sizes.setdefault(key, 0)
                field_sizes[key] += sys.getsizeof(value)
        for key, total_size in field_sizes.items():
            avg_field_size = total_size / total_records
            f.write(f"Average size of field '{key}': {avg_field_size:.2f} bytes\n")
        
        f.write(f"Analysis for collection '{collection_name}' completed.\n\n")

def main():
    # Connect to MongoDB
    config = load_config()
    client = MongoClient(config["MONGODB_URI"])
    db = client["movies&shows"]  

    # Collections to analyze
    collections = ["movies&shows", "users", "interactions"]

    # Output file for analysis results
    output_file = "dataset_analysis.txt"
    
    # Clear previous results
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("Dataset Analysis Report\n")
        f.write("=" * 50 + "\n\n")

    # Analyze each collection
    for collection_name in collections:
        collection = db[collection_name]
        data = load_data_from_mongodb(collection)
        dataset_size(data, collection_name, output_file)

    print(f"Analysis for all collections has been written to '{output_file}'.")

if __name__ == '__main__':
    main()