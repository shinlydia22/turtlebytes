from flask import Flask, request, jsonify
import os
from datetime import datetime

app = Flask(__name__)
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/uploadfile', methods=['POST'])
def upload_file():
    if 'myFile' not in request.files:
        return jsonify({'error': 'No file provided'}), 400

    file = request.files['myFile']

    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if not allowed_file(file.filename):
        return jsonify({'error': 'Invalid file type'}), 400

    file_data = file.read()
    
    # Generate a unique filename based on the current timestamp
    unique_filename = f'{datetime.now().strftime("%Y%m%d%H%M%S")}_{file.filename}'
    file_path = os.path.join('uploads', unique_filename)

    with open(file_path, 'wb') as f:
        f.write(file_data)

    return jsonify({'message': 'File uploaded successfully'})

import subprocess

@app.route('/api/analyze-image', methods=['POST'])
def analyze_image():
    unique_filename = request.json.get('unique_filename')
    image_path = os.path.join('uploads', unique_filename)

    try:
        subprocess.check_call(['jupyter', 'nbconvert', '--to', 'notebook', '--execute', 'your_analysis_notebook.ipynb', '--ExecutePreprocessor.timeout=600', '--output', 'output.ipynb', '--unique_filename', image_path])
    except subprocess.CalledProcessError as e:
        return jsonify({'error': 'Image analysis failed'}), 500

    return jsonify({'message': 'Image analysis started'})

if __name__ == '__main__':
    app.run()