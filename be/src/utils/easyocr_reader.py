import easyocr

def init_easyocr():
    return easyocr.Reader(['en'], gpu=False)

def recognize_text(reader, image):
    results = reader.readtext(image)
    return [res[1] for res in results]