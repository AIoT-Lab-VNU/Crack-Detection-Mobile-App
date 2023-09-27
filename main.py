import matplotlib.pyplot as plt
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager, NoTransition
from kivy.uix.camera import Camera
import torch
import cv2
import numpy as np
from PIL import Image
import torchvision.transforms as transforms
from torchvision.models.detection import (
    fasterrcnn_resnet50_fpn_v2,
    FasterRCNN_ResNet50_FPN_V2_Weights,
)
from model import DetectNet

# Loading pretrained model
weights = FasterRCNN_ResNet50_FPN_V2_Weights.DEFAULT
object_model = fasterrcnn_resnet50_fpn_v2(weights=weights)
save_detect = "detect.jpg"

# Instantiate model
model = DetectNet(object_model, weights=weights, save_name=save_detect)


class Header(Widget):
    pass


class OpenCamera(Camera):
    pass


class CrackContainer(ScreenManager):
    pass


class CrackContainer1(Screen):
    pass


class CrackContainer2(Screen):
    start_cam = ObjectProperty(None)
    close_cam = ObjectProperty(None)

    def capture(self):
        print("Captured!")

        # Take out raw pixels
        camera = self.ids["camera"]
        raw = camera.texture.pixels
        size = camera.texture.size

        # Convert image to Tensor
        image = Image.frombuffer(mode="RGBA", size=size, data=raw)
        image = image.convert("RGB")
        # transform = transforms.Compose([(transforms.ToTensor())])
        # tensor_img = transform(np.array(image))
        # tensor_img = tensor_img.to(torch.uint8)
        # tensor_img = tensor_img.permute(1, 2, 0).numpy()
        image = np.transpose(np.array(image), (2, 0, 1))
        image = torch.from_numpy(image).to(torch.uint8)

        # Detect and save
        model(image)


class CrackApp(App):
    def build(self):
        # Initialize container for whole app
        sm = ScreenManager(transition=NoTransition())
        screen1 = CrackContainer1(name="first")
        screen2 = CrackContainer2(name="second")

        sm.add_widget(screen1)
        sm.add_widget(screen2)

        return sm


if __name__ == "__main__":
    CrackApp().run()
