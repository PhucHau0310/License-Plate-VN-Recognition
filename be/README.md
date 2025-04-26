# 📄 README.md

# License Plate Recognition

Detect biển số xe Việt Nam và trích xuất số bằng OCR.

-   YOLOv8 để detect
-   EasyOCR hoặc PaddleOCR để đọc số

```bash
python pipeline/run_pipeline.py
```

Hoặc chạy API:

```bash
uvicorn app.main:app --reload
```
