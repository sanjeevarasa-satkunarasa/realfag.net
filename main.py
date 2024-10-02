import os
import subprocess
import pymongo

# MongoDB connection setup
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Select the database
db = client["admin"]

# Create or get the collection with collation for Norwegian characters
try:
    collection = db.create_collection(
        "results",
        collation={"locale": "nb"}
    )
except pymongo.errors.CollectionInvalid:
    collection = db.get_collection(
        "results",
        collation={"locale": "nb"}
    )

# Function to insert into MongoDB
def insert_mongodb(key, value):
    document = {"key": key, "value": value}
    result = collection.insert_one(document)
    print("Document inserted with ID:", result.inserted_id)

# Directory containing the PDF files
directory = r'G:\My Drive\Personal\Programming\Projects\OCR Question Bank\OCR-Question-Finder\eksamensoppgaver'

# Function to convert Windows path to WSL path
def convert_to_wsl_path(win_path):
    return subprocess.run(['wsl', 'wslpath', '-a', win_path], capture_output=True, text=True).stdout.strip()

# Function to process PDF files
def process_pdfs(directory):
    for root, _, files in os.walk(directory):
        for filename in files:
            if filename.endswith('.pdf'):
                pdf_path = os.path.join(root, filename)
                wsl_pdf_path = convert_to_wsl_path(pdf_path)
                output_file = os.path.join(root, f'{os.path.splitext(filename)[0]}_output.pdf')
                wsl_output_file = convert_to_wsl_path(output_file)
                sidecar_file = os.path.join(root, f'{os.path.splitext(filename)[0]}.txt')
                wsl_sidecar_file = convert_to_wsl_path(sidecar_file)
                
                try:
                    print(f'PDF path: {pdf_path} (WSL: {wsl_pdf_path})')
                    print(f'Output file path: {output_file} (WSL: {wsl_output_file})')
                    print(f'Sidecar file path: {sidecar_file} (WSL: {wsl_sidecar_file})')
                    
                    result = subprocess.run(['wsl', 'ocrmypdf', '-l', 'nor', '--sidecar', wsl_sidecar_file, '--force-ocr', wsl_pdf_path, wsl_output_file], check=True, capture_output=True, text=True)
                    print(f'ocrmypdf command result: {result}')
                    print(f'Stdout: {result.stdout}')
                    print(f'Stderr: {result.stderr}')
                    
                    if os.path.exists(sidecar_file):
                        print(f'Sidecar file created: {sidecar_file}')
                        with open(sidecar_file, 'r', encoding='utf-8') as file:
                            content = file.read()
                        insert_mongodb(filename, content)
                    else:
                        print(f'Sidecar file not found: {sidecar_file}')
                except subprocess.CalledProcessError as e:
                    print(f'Error processing {pdf_path}: {e}')
                    print(f'Stdout: {e.stdout}')
                    print(f'Stderr: {e.stderr}')
                except Exception as e:
                    print(f'Unexpected error: {e}')

# Start processing
process_pdfs(directory)

print("Processing complete.")
