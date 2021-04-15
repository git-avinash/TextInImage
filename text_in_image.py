from PIL import Image
import pytesseract
import sys
import cv2

# Default Installation path when installed for everyone
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Custom Path
pytesseract.pytesseract.tesseract_cmd = r"./Tesseract-OCR/tesseract.exe"

def make_grey_scale(image_name):
    img = cv2.imread(image_name)
    grey_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite("grey_scaled.png", grey_image)

def get_text(image_name):
    make_grey_scale(image_name)

    with Image.open("grey_scaled.png") as image:
        text = pytesseract.image_to_string(image, lang="eng")

    return text


print(get_text(sys.argv[1]))
