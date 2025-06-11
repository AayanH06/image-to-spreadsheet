import pytesseract
import cv2

from PIL import Image, ImageEnhance

image = Image.open('image.png')

data = pytesseract.image_to_data(
    image,
    output_type=pytesseract.Output.DICT
)

print(data)