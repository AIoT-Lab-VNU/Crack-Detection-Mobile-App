import torch
import cv2
import numpy as np
from torchvision.io import read_image
from PIL import Image
import torchvision.transforms as transforms
from torchvision.utils import draw_bounding_boxes
from torchvision.transforms.functional import to_pil_image
import torch.nn as nn
from ultralytics import YOLO


class DetectNet(nn.Module):
    def __init__(self, model, save_name):
        super().__init__()
        self.model = model
        self.save_name = save_name

    def forward(self, img):

        # Prediction
        prediction = self.model(img)
        detect_img = prediction[0].plot()

        # Save detected image
        cv2.imwrite(self.save_name, detect_img)


if __name__ == "__main__":
    print("Test")
    #img = "crack2.jpg"

    # Load pretrained model
    #yolo = YOLO("weights/best.pt")
    #save_dir = "detect_crack.png"

    # Instantiate model
    #model = DetectNet(yolo, save_name=save_dir)

    # Predict image
    #image = cv2.imread(img)

    # Predict & Save
    #model(image)
