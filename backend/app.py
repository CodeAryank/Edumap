from flask import Flask, request, jsonify, send_from_directory
from werkzeug.utils import secure_filename, safe_join
import os
from flask_cors import CORS
from transformers import pipeline
import PyPDF2
from hugging_phase import get_variable

app = Flask(__name__)
CORS(app)

# Configuration
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Load the summarizer model
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def extract_text_from_pdf(file_path):
    text = ""
    with open(file_path, "rb") as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
        for page in reader.pages:
            text += page.extract_text()
    return text

def summarize_text(text, max_chunk_length=500):
    chunks = [text[i:i + max_chunk_length] for i in range(0, len(text), max_chunk_length)]
    summaries = []
    for chunk in chunks:
        current_max_length = min(100, len(chunk))
        summary = summarizer(chunk, max_length=current_max_length, min_length=25, truncation=True)[0]['summary_text']
        summaries.append(summary)
    return " ".join(summaries)

@app.route('/upload', methods=['POST'])
def upload_files():
    if 'files' not in request.files:
        return jsonify({"success": False, "error": "No files part"}), 400

    files = request.files.getlist('files')
    download_urls = []
    
    for file in files:
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            download_urls.append(f"/download/{filename}")
    
    return jsonify({"success": True, "downloadUrls": download_urls})

@app.route('/download/<filename>')
def download_file(filename):
    try:
        return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@app.route('/get-summary', methods=['GET'])
def get_summary():
    try:
        folder_path = app.config['UPLOAD_FOLDER']
        combined_text = ""
        
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            if filename.endswith('.pdf'):
                combined_text += extract_text_from_pdf(file_path)
            elif filename.endswith('.txt'):
                with open(file_path, 'r', encoding='utf-8') as f:
                    combined_text += f.read()

        if not combined_text.strip():
            return jsonify({"success": False, "error": "No valid text found in files"}), 400

        #final_summary = summarize_text(combined_text)
        final_summary = get_variable()
        return jsonify({"success": True, "summary": final_summary})

    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)
