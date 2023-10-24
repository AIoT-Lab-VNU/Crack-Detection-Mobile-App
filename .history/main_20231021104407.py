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


class CrackContainer(ScreenManager):
    pass

class CrackContainer1(Screen):
    start_cam = ObjectProperty(None)
    close_cam = ObjectProperty(None)  # Thêm thuộc tính close_cam

    def capture_image(self):
        self.ids["camera"].export_to_png(save_dir)  # Lưu ảnh đã chụp
        self.ids["camera"].play = False  # Dừng camera
        self.ids["start_cam"].disabled = True  # Ẩn nút chụp
        app = App.get_running_app()
        app.root.current = "second"  # Chuyển sang CrackContainer2 để hiển thị kết quả



class CrackContainer2(Screen):
    close_cam = ObjectProperty(None)
    detect_img = ObjectProperty(None)
    report = ObjectProperty(None)

    def capture(self):
        print("Captured!")

        # Take out raw pixels
        camera = self.ids["camera"]
        raw = camera.texture.pixels
        size = camera.texture.size
        print(size)

        # Convert image to Tensor
        image = PILImage.frombuffer(mode="RGBA", size=size, data=raw)
        image = image.convert("RGB")
        image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

        # Detect and save
        result = model(image)

        # Display the detected image on the screen
        detected_image = self.ids["detect_img"]
        detected_image.source = save_dir

        # Print out result
        report = self.ids["report"]

        if len(result) == 0:
            report.text = "No crack found"
        elif len(result) == 1:
            area, score = result[0]
            report.text = (
                f"Crack predicted accuracy: "
                + "%.2f" % score
                + " %\nThe area of crack is: "
                + "%.2f" % area
                + " cm²"
            )
        else:
            text = ""
            for i, out in enumerate(result):
                area, score = out
                text += (
                    f"Crack {i+1} predicted accuracy: "
                    + "%.2f" % score
                    + f" %\nThe area of crack {i+1} is: "
                    + "%.2f" % area
                    + " cm²\n\n"
                )
            report.text = text

        # Chuyển sang CrackContainer3 để hiển thị kết quả
        app = App.get_running_app()
        app.root.current = "third"

class CrackContainer3(Screen):
    report_text = ObjectProperty(None)

    def on_enter(self, *args):
        super().on_enter(*args)
        # Hiển thị nội dung về vết nứt ở đây



class CrackApp(App):
    def build(self):
        # Initialize container for whole app
        sm = ScreenManager(transition=NoTransition())
        screen1 = CrackContainer1(name="first")
        screen2 = CrackContainer2(name="second")
        screen3 = CrackContainer3(name="third")

        sm.add_widget(screen1)
        sm.add_widget(screen2)
        sm.add_widget(screen3)

        return sm

if __name__ == "__main__":
    CrackApp().run()