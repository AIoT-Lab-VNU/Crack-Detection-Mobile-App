import torch
import cv2
import numpy as np
from torchvision.models.detection import (
    fasterrcnn_resnet50_fpn_v2,
    FasterRCNN_ResNet50_FPN_V2_Weights,
)
from torchvision.io import read_image
from PIL import Image
import torchvision.transforms as transforms
from torchvision.utils import draw_bounding_boxes
from torchvision.transforms.functional import to_pil_image
import torch.nn as nn


class DetectNet(nn.Module):
    def __init__(self, object_model, weights, save_name):
        super().__init__()
        self.object_model = object_model
        self.weights = weights
        self.save_name = save_name

    def forward(self, img):
        # Inference
        self.object_model.eval()

        # Preprocess
        preprocess = self.weights.transforms()
        image = [preprocess(img)]

        # Prediction
        prediction = self.object_model(image)[0]
        labels = [self.weights.meta["categories"][i] for i in prediction["labels"]]
        box = draw_bounding_boxes(
            img, boxes=prediction["boxes"], labels=labels, colors="red", width=4
        )

        im = to_pil_image(box.detach())
        im = Image.fromarray(np.array(im))
        im.save(self.save_name)


if __name__ == "__main__":
    print("")
    # weights = FasterRCNN_ResNet50_FPN_V2_Weights.DEFAULT
    # object_model = fasterrcnn_resnet50_fpn_v2(weights=weights)
    # save_dir = "test.png"
    #
    # model = DetectNet(object_model, weights=weights, save_name=save_dir)
    #
    # imgs = "several_box.jpg"
    # img = read_image(imgs)
    # img = img[:3]
    #
    # model(img)
