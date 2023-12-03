    # /app/routes.py
from app import app
from flask import render_template,request
from transformers import pipeline
from PIL import Image
import io
import os
import tempfile

def captioning(image):
    captioner = pipeline("image-to-text",model="Salesforce/blip-image-captioning-base")
    return captioner(image)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Check if the POST request has the file part
        if 'image' not in request.files:
            return render_template('index.html', message='No file part')

        image = request.files['image']
        # Save the received image to a temporary file
        temp_dir = tempfile.gettempdir()
        # temp_image_path = os.path.join(temp_dir, image.filename)
        temp_fd, temp_image_path = tempfile.mkstemp(suffix='_' + image.filename, dir=temp_dir)
        image.save(temp_image_path)
        #image = Image.open(io.BytesIO(file.read()))
        #print(type(image))
        print(temp_image_path)
        # 
        msg = captioning(temp_image_path)
        msg = msg[0]['generated_text']
        os.remove(temp_image_path)

        # If the user does not select a file, the browser submits an empty file without a filename
        if image.filename == '':
            return render_template('index.html', message='No selected file')

        # You can process the image as needed here (e.g., save it to a folder or a database)
        print(f"Received image: {msg}")
        return render_template('generate.html',message=msg)

    return render_template('index.html')

@app.route('/generate', methods=['GET', 'POST'])
def generate():
    return render_template('index.html')