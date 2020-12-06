from PIL import Image
import pytesseract
import sys

# Default Installation path when installed for everyone
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Custom Path
pytesseract.pytesseract.tesseract_cmd = r".\Tesseract-OCR\tesseract.exe"


def get_text(image_name):
    with Image.open(image_name) as image:
        text = pytesseract.image_to_string(image, lang="eng")

    return text


print(get_text(sys.argv[1]))
