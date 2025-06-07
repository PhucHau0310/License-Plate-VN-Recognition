# 🚀 Vietnamese License Plate Recognition

This project uses YOLOv8 to detect license plates and EasyOCR to recognize text from images.

## ✨ Training Process

### 📈 Training Pipeline

![Training Pipeline](be/src/Reports/training_pipeline.gv.png)

### 📈 Training Results

#### Loss and Metrics

![Training Results](be/src/Reports/results.png)

#### Precision-Recall Curve

![PR Curve](be/src/Reports/PR_curve.png)

#### Confusion Matrix

![Confusion Matrix](be/src/Reports/confusion_matrix_normalized.png)

## 🔌 API Pipeline

### Processing Flow

![API Pipeline](be/src/Reports/pipeline_diagram.gv.png)

### 📸 Screenshots

![Sample Output](be/src/Reports/output_image_sample.png)

### 📁 Project Structure

```
root/
├── be/
│   ├── src/
│   │   ├── models/
|   |   ├── app/
|   |	├── data/
│   │   ├── reports/
│   │   └── utils/
│   ├── Dockerfile
│   └── requirements.txt
├── fe/
│   ├── src/
│   │   ├── app/
│   │   └── public/
│   ├── Dockerfile
│   └── package.json
├── docker-compose.yml
└── README.md
```

### 📦 Installation

```bash
git clone https://github.com/PhucHau0310/License-Plate-VN-Recognition.git
cd root project
docker-compose up -d --build
```

### 📜 License

This project is licensed under the MIT License.

### 👤 Author

-   GitHub: PhucHau0310
-   Email: haunhpr024@gmail.com
