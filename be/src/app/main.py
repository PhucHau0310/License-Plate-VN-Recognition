from fastapi import FastAPI, UploadFile, File
import shutil
import cv2
import os
from utils.detect_plate import load_model, detect_plate, crop_plate
from utils.easyocr_reader import init_easyocr, recognize_text
import base64
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Vietnamese License Plate Recognition API",
    version="1.0.0",
    description="API for recognizing Vietnamese license plates from images"
)

origins = ["http://localhost:3000", "http://127.0.0.1:3000", "http://localhost:4002", "http://127.0.0.1:4002", 
           "https://license-plate-recognition-fe.hau.io.vn", "https://license-plate-recognition-fe.hau.io.vn:4002",
           "https://license-plate-recognition-fe.hau.io.vn:3000"]

app.add_middleware(
CORSMiddleware,
allow_origins=origins,
allow_credentials=True,
allow_methods=["*"],
allow_headers=["*"],
)

model = load_model("models/yolov8_plate.pt")
reader = init_easyocr()

# Root endpoint
@app.get("/", 
    summary="API Home",
    description="Endpoint to check if API is running")
async def read_root():
    return {
        "message": "Vietnamese License Plate Recognition API",
        "version": "1.0.0",
        "status": "running",
        "endpoints": {
            "detect plate through image": "/detect - POST (form-data with file)"
        }
    }

@app.post("/detect", summary="Detect license plate",
    description="Endpoint to detect license plate from an image and return image with marked plate")
def upload_image(file: UploadFile = File(...)):
    with open("temp.jpg", "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    # Run detection and recognition
    text, bbox, output_image = run_with_visualization("temp.jpg", model, reader)
    
    # Encode the image to base64 for JSON response
    _, img_encoded = cv2.imencode('.jpg', output_image)
    img_base64 = base64.b64encode(img_encoded).decode('utf-8')
    
    # Clean up
    if os.path.exists("temp.jpg"):
        os.remove("temp.jpg")
    
    return {
        "plate_text": text,
        "image_base64": img_base64
    }

def run_with_visualization(image_path, model, reader):
    """Run the pipeline and return the text, bounding box, and visualized image"""
    image = cv2.imread(image_path)
    detections = detect_plate(model, image)
    
    if len(detections) == 0:
        return "No plate detected", None, image
    
    # Get the first detected plate
    bbox = detections[0]
    plate_crop = crop_plate(image, bbox)
    text = recognize_text(reader, plate_crop)
    
    # Prepare the text string for display
    text_str = ", ".join(text) if text else "No text detected"
    
    # Draw bounding box and text on the original image
    output_image = image.copy()
    x1, y1, x2, y2 = map(int, bbox[:4])
    cv2.rectangle(output_image, (x1, y1), (x2, y2), (0, 255, 0), 2)
    cv2.putText(output_image, text_str, (x1, y1-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
    
    return text_str, bbox, output_image
