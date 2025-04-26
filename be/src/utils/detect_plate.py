import cv2
from ultralytics import YOLO

def load_model(weights):
    return YOLO(weights)

def detect_plate(model, image):
    results = model(image)
    return results[0].boxes.data.cpu().numpy()

def crop_plate(image, bbox):
    x1, y1, x2, y2 = map(int, bbox[:4])
    return image[y1:y2, x1:x2]
