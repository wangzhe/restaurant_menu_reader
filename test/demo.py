import argparse
import os

import cv2
import pytesseract
from PIL import Image

from model.image_processor import preprocess_image

image = None
gray = None


def cmd_args(ap=None):
    # construct the argument parse and parse the arguments
    if ap is None: return None
    ap.add_argument("-i", "--image", required=True, help="path to input image to be OCR'd")
    ap.add_argument("-p", "--preprocess", type=str, default="thresh", help="type of preprocessing to be done")
    return vars(ap.parse_args())


def ocr_image(filename, config):
    # load the image as a PIL/Pillow image, apply OCR, and then delete the temporary file
    text = pytesseract.image_to_string(image=Image.open(filename), config=config)
    os.remove(filename)
    print("the image content: %s", text)


def show_image():
    global image, gray
    cv2.imshow("Image", image)
    cv2.imshow("Output", gray)
    cv2.waitKey(0)


if __name__ == '__main__':
    # retrieve parameters
    args = cmd_args(argparse.ArgumentParser())

    # generate pre-process the image
    if args is None: exit(1)
    proceed_image_name = preprocess_image(args)

    # ocr by tesseract
    custom_config = r'--oem 3 --psm 6'
    ocr_image(proceed_image_name, custom_config)

    # show the output images
    show_image()
