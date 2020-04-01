import cv2
import numpy
import pytesseract
from PIL import Image


# process image with name
def preprocess_image_with_filename(image_filename, preprocess):
    # load the example source_image and convert it to grayscale
    source_image = cv2.imread(image_filename)
    proceed_image = preprocess_image(source_image, preprocess)
    return source_image, proceed_image


# process image with the PIL image object
def preprocess_image(image, mode):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # check to see if we should apply thresholding to preprocess the image
    if mode == "thresh":
        gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

    # make a check to see if median blurring should be done to remove noise
    elif mode == "blur":
        gray = cv2.medianBlur(gray, 3)

    return gray


# put the proceed PIL image to ocr tesseract
def ocr_image(image):
    # pre-process images
    cv_image = cv2.cvtColor(numpy.asarray(image), cv2.COLOR_RGB2BGR)
    proceed_image = preprocess_image(cv_image, "thresh")

    # load the image as a PIL/Pillow image, apply OCR, and then delete the temporary file
    custom_config = r'--oem 3 --psm 6'
    text = pytesseract.image_to_string(image=proceed_image, config=custom_config)
    text = text.strip()
    return text
