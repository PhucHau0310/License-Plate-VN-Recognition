# Vietnamese License Plate Recognition

## Overview

This project uses YOLOv8 to detect license plates and EasyOCR to recognize text from images.

## Training Process

### Training Pipeline

![Training Pipeline](be/src/Reports/training_pipeline.gv.png)

### Training Results

#### Loss and Metrics

![Training Results](be/src/Reports/results.png)

#### Precision-Recall Curve

![PR Curve](be/src/Reports/PR_curve.png)

#### Confusion Matrix

![Confusion Matrix](be/src/Reports/confusion_matrix_normalized.png)

## API Pipeline

### Processing Flow

![API Pipeline](be/src/Reports/pipeline_diagram.gv.png)

### Sample Output

![Sample Output](be/src/Reports/output_image_sample.png)

### Run Project with dockercompose

Cd root project run docker-compose up -d --build
