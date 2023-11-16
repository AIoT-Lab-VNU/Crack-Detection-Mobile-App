from flask import Flask, request, jsonify
import torch
import cv2
import numpy as np
from PIL import Image
from model import DetectNet
from utils import decode_image
from ultralytics import YOLO
from flask_cors import CORS
import os
import base64
import io

app = Flask(__name__)
CORS(app, resources={r'/*': {'origins': '*'}})

@app.route("/")
def hello_world():
    return "<h1>Welcome to Crack Detection App</h1>"

@app.route('/process-image', methods=['POST'])
def process_image():
    try:
        print('Receiving request')
        # print(request.get_json()['base64'])
        img_base64 = request.get_json()['base64']

        if img_base64 == '':
            return jsonify({'error': 'No image uploaded'}) 
        
        image_data = base64.b64decode(img_base64)
        image = Image.open(io.BytesIO(image_data))
        image = image.resize((320, 240))
        
        yolo = YOLO("weights/best.pt")
        save_dir = "result.png"
        model = DetectNet(yolo, save_name=save_dir)
        result = model(image)

        image = decode_image("result.png")
        # return jsonify({'image': image, 'result': str(result)})
        print(str(image))
        return jsonify({'image': str(image), 'result': str(result)})


    except Exception as ex:
        print(ex)
        return jsonify({'error': str(ex)})
    
@app.route('/process-selected-image', methods=['POST'])
def process_selected_image():
    try:
        print('Receiving request')
        # print(request.get_json()['base64'])
        img_base64 = request.get_json()

        if img_base64 == '':
            return jsonify({'error': 'No image uploaded'}) 
        
        image_data = base64.b64decode(img_base64)
        image = Image.open(io.BytesIO(image_data))
        image = image.resize((320, 240))
        
        yolo = YOLO("weights/best.pt")
        save_dir = "result.png"
        model = DetectNet(yolo, save_name=save_dir)
        result = model(image)

        image = decode_image("result.png")
        # return jsonify({'image': image, 'result': str(result)})
        print(str(image))
        return jsonify({'image': str(image), 'result': str(result)})


    except Exception as ex:
        print(ex)
        return jsonify({'error': str(ex)})
        

if __name__ == "__main__":
    app.run()