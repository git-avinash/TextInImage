from PIL import Image
import pytesseract
import sys

# Default Installation path when installed for everyone
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Custom Path
pytesseract.pytesseract.tesseract_cmd = r".\Tesseract-OCR\tesseract.exe"

with Image.open(sys.argv[1]) as image:
    text = pytesseract.image_to_string(image, lang="eng")

# image = Image.open("test.png")
# text = pytesseract.image_to_string(image, lang="eng")

print(text)
