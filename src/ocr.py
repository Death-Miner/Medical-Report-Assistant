import pytesseract
from PIL import Image


# Change this path if Tesseract is installed somewhere else
pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)


def extract_image_text(image_path):
    image = Image.open(image_path)

    text = pytesseract.image_to_string(image)

    return text