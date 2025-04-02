import unittest
from PIL import Image
import pytesseract

class TestOCR(unittest.TestCase):
    def test_ocr_on_sample_image(self):
        # Load a sample image
        image_path = r"C:\Users\deser\overlay_ai\image.png"
        image = Image.open(image_path)

        # Perform OCR
        text = pytesseract.image_to_string(image)

        # Assert that text is not empty
        self.assertTrue(len(text.strip()) > 0, "OCR output is empty")

if __name__ == "__main__":
    unittest.main()