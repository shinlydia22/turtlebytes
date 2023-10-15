from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from datetime import datetime
import subprocess

app = Flask(__name__)
CORS(app)
ALLOWED_EXTENSIONS = {'png', 'jpg'}

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
    
    if file:
        # Save the uploaded file to a folder on the server
        file.save('uploads/' + file.filename)
        return "File uploaded successfully"


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
    try:
        subprocess.check_call(['jupyter', 'nbconvert', '--to', 'notebook', '--execute', 'your_analysis_notebook.ipynb', '--ExecutePreprocessor.timeout=600', '--output', 'output.ipynb', '--unique_filename', image_path])
    except subprocess.CalledProcessError as e:
        return jsonify({'error': 'Image analysis failed'}), 500

    # Further processing to extract or format the results from the executed notebook

    return jsonify({'message': 'Image analysis completed'})


if __name__ == '__main__':
    app.run(debug=True, port=5000)
