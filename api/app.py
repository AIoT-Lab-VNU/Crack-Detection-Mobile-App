from flask import Flask, request, jsonify
import torch
import cv2
import numpy as np
from PIL import Image
from model import DetectNet
from utils import decode_image
from ultralytics import YOLO
import os

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Welcome to Crack Detection App</h1>"

@app.route('/process-image', methods=['POST'])
def process_image():
    try:
        # Check if an image was uploaded
        if 'image' not in request.files:
            return jsonify({'error': 'No image uploaded'})

        image = request.files['image']

        # Ensure it's a valid image format (e.g., JPEG)
        if image.filename == '':
            return jsonify({'error': 'No selected file'})
        
        if image:
            image = Image.open(image)
            yolo = YOLO("weights/best.pt")
            save_dir = "result.png"
            model = DetectNet(yolo, save_name=save_dir)
            result = model(image)

            image = decode_image("result.png")
            # print(image)
            response = {
                'image': str(image),
                'result': str(result)
            }

            return jsonify(response)


    except Exception as ex:
        print(ex)
        return jsonify({'error': str(ex)})
        

if __name__ == "__main__":
    app.run()