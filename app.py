from flask import Flask, request, redirect, url_for, flash, render_template
import os
import subprocess
import pymongo
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import re
from PIL import Image

from flask import Flask, request, redirect, url_for, flash, render_template
import pymongo

app = Flask(__name__)
app.secret_key = 'supersecretkey'
app.config['UPLOAD_FOLDER'] = 'uploads'

# MongoDB connection setup
client = pymongo.MongoClient("mongodb+srv://ssanjeevarasa:9m8QBUEEQjW9pysP@results.szk52.mongodb.net/?retryWrites=true&w=majority&appName=results")
db = client["admin"]
# Get the collection
collection = db["results"]

# Function to insert into MongoDB
def insert_mongodb(key, value):
    document = {"key": key, "value": value}
    result = collection.insert_one(document)
    print("Document inserted with ID:", result.inserted_id)

# Function to convert Windows path to WSL path
def convert_to_wsl_path(win_path):
    return subprocess.run(['wsl', 'wslpath', '-a', win_path], capture_output=True, text=True).stdout.strip()

# Function to convert image files to PDF
def convert_image_to_pdf(image_path):
    image = Image.open(image_path)
    pdf_path = os.path.splitext(image_path)[0] + '.pdf'
    image.save(pdf_path, 'PDF', resolution=100.0)
    return pdf_path

# Function to process files
def process_file(file_path):
    if file_path.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tiff')):
        file_path = convert_image_to_pdf(file_path)
    
    wsl_file_path = convert_to_wsl_path(file_path)
    output_file = os.path.splitext(file_path)[0] + '_output.pdf'
    wsl_output_file = convert_to_wsl_path(output_file)
    sidecar_file = os.path.splitext(file_path)[0] + '.txt'
    wsl_sidecar_file = convert_to_wsl_path(sidecar_file)
    
    try:
        result = subprocess.run(['wsl', 'ocrmypdf', '-l', 'nor', '--sidecar', wsl_sidecar_file, '--force-ocr', wsl_file_path, wsl_output_file], check=True, capture_output=True, text=True)
        
        if os.path.exists(sidecar_file):
            with open(sidecar_file, 'r', encoding='utf-8') as file:
                content = file.read()
            return content
        else:
            return 'Sidecar file not found'
    except subprocess.CalledProcessError as e:
        return f'Error processing {file_path}: {e}'
    except Exception as e:
        return f'Unexpected error: {e}'

# Function to get the most similar document key
def get_most_similar_document_key(input_string, db_name, collection_name):
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client[db_name]
    collection = db[collection_name]

    documents = list(collection.find({}, collation={"locale": "nb"}))
    keys = [doc.get("key") for doc in documents]
    values = [doc.get("value", "") for doc in documents]

    values.append(input_string)

    vectorizer = TfidfVectorizer().fit_transform(values)
    vectors = vectorizer.toarray()

    cosine_similarities = cosine_similarity(vectors[-1:], vectors[:-1]).flatten()

    most_similar_index = np.argmax(cosine_similarities)
    most_similar_key = keys[most_similar_index]

    return most_similar_key

# Function to format output
def format_output(output):
    if output:
        output = output.replace(".pdf", "").replace("_", " ")
    return output

# Flask routes
@app.route('/')
def index():
    return render_template('index.html', output="")

@app.route('/upload', methods=['POST'])
def upload_file():
    text = request.form.get('question-text')
    file = request.files.get('file-upload')

    if text and file:
        flash("Det kan ikke være to inputter")
        return redirect(url_for('index'))
    elif file:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)
        ocr_output = process_file(file_path)
        output = format_output(get_most_similar_document_key(ocr_output, "admin", "results"))
    elif text:
        normalized_text = re.sub(r'\W+', ' ', text.lower())
        output = format_output(get_most_similar_document_key(normalized_text, "admin", "results"))
    else:
        output = "No input provided"

    return render_template('index.html', output=output)

@app.route('/static/templates/index.html')
def index2():
    return render_template('index.html')

@app.route('/static/templates/VG3.html')
def VG3():
    return render_template('VG3.html')

@app.route('/static/templates/VG2.html')
def VG2():
    return render_template('VG2.html')

@app.route('/static/templates/VG1.html')
def VG1():
    return render_template('VG1.html')

@app.route('/static/templates/info.html')
def info():
    return render_template('info.html')

@app.route('/static/templates/logg.html')
def logg():
    return render_template('logg.html')

if __name__ == '__main__':
    app.run(debug=True)
