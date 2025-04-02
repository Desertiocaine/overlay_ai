import pytesseract

try:
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    version = pytesseract.get_tesseract_version()
    print(f"Tesseract is configured correctly! Version: {version}")
except Exception as e:
    print(f"Error configuring Tesseract: {e}")