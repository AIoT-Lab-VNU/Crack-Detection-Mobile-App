import matplotlib.pyplot as plt
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager, NoTransition
from kivy.uix.camera import Camera
from kivy.uix.popup import Popup
from kivy.core.window import Window
Window.size = (430, 932)
import torch
import cv2
import numpy as np
from PIL import Image as PILImage
from kivy.uix.image import Image
import torchvision.transforms as transforms
from model import DetectNet
from ultralytics import YOLO
import os

# Loading pretrained model
yolo = YOLO("weights/best.pt")
save_dir = "detect.png"

# Instantiate model
model = DetectNet(yolo, save_name=save_dir)


class Header(Widget):
    pass


class OpenCamera(Camera):
    pass

class CrackContainer1(Screen):
    start_cam = ObjectProperty(None)
    close_cam = ObjectProperty(None)
    detect_img = ObjectProperty(None)
    report = ObjectProperty(None)



    def remove_img(self):
        detected_image = self.ids["detect_img"]
        detected_image.nocache = True
        detected_image.source = ""

    def remove_result(self):
        self.report.nocache = True
        self.report.text = ""


class CrackApp(App):
    def build(self):
        sm = ScreenManager(transition=NoTransition())
        screen1 = CrackContainer1(name="first")
        sm.add_widget(screen1)
        return sm


if __name__ == "__main__":
    CrackApp().run()
#check