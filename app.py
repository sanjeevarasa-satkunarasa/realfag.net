import os
import re
from flask import Flask, request, redirect, url_for, flash, render_template
from flask_mail import Mail, Message
import subprocess
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from PIL import Image

app = Flask(__name__)
app.secret_key = 'supersecretkey'
app.config['UPLOAD_FOLDER'] = 'uploads/'

# Ensure the upload folder exists
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

# Configure Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.privateemail.com'
app.config['MAIL_PORT'] = 465  # Use 587 for TLS/STARTTLS
app.config['MAIL_USE_SSL'] = True  # Use False if using TLS/STARTTLS
app.config['MAIL_USERNAME'] = 'contact@realfag.net'
app.config['MAIL_PASSWORD'] = 'EtArg2mApbY)(rP'

mail = Mail(app)

# Function to load data from JSON
def load_data():
    try:
        with open('data.json', 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
        return {item['key']: item['value'] for item in data}
    except FileNotFoundError:
        return {}

# Function to save data as JSON
def save_data(data):
    existing_data = load_data()
    existing_data.update(data)
    formatted_data = [{'_id': {'$oid': str(i)}, 'key': k, 'value': v} for i, (k, v) in enumerate(existing_data.items())]
    with open('data.json', 'w', encoding='utf-8') as json_file:
        json.dump(formatted_data, json_file, indent=4)

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
    output_file = os.path.splitext(file_path)[0] + '_output.pdf'
    sidecar_file = os.path.splitext(file_path)[0] + '.txt'
    
    try:
        result = subprocess.run(['ocrmypdf', '-l', 'nor', '--sidecar', sidecar_file, '--force-ocr', file_path, output_file], check=True, capture_output=True, text=True)
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
def get_most_similar_document_key(input_string):
    data = load_data()
    keys = list(data.keys())
    values = list(data.values())
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
    
    output = "No input provided"
    
    if file:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)
        ocr_output = process_file(file_path)
        output = format_output(get_most_similar_document_key(ocr_output))

    elif text:
        normalized_text = re.sub(r'\W+', ' ', text.lower())
        output = format_output(get_most_similar_document_key(normalized_text))

    return render_template('index.html', output=output)

@app.route('/send_email', methods=['POST'])
def send_email():
    year = request.form['year']
    school = request.form['school']
    resource_type = request.form['resource_type']
    file = request.files['file']

    msg = Message(subject=f"New Submission: {resource_type}",
                  sender='contact@realfag.net',
                  recipients=['contact@realfag.net'])
    msg.body = f"Year: {year}\nSchool: {school}\nResource Type: {resource_type}"

    if file:
        filename = file.filename
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        with app.open_resource(file_path) as fp:
            msg.attach(filename, "application/octet-stream", fp.read())

    mail.send(msg)
    flash("Email sent successfully!")
    return redirect(url_for('index'))

@app.route('/send_problem', methods=['POST'])
def send_problem():
    problem_text = request.form['problem-text']
    
    msg = Message(subject="Problem Report", sender='contact@realfag.net', recipients=['contact@realfag.net'])
    msg.body = f"Problem reported:\n\n{problem_text}"
    
    mail.send(msg)
    flash("Problem reported successfully!")
    return redirect(url_for('index'))

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
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=True)