import argparse

import cv2

from model.image_processor import preprocess_image_with_filename, ocr_image

image = None
gray = None


def cmd_args(ap=None):
    # construct the argument parse and parse the arguments
    if ap is None: return None
    ap.add_argument("-i", "--image", required=True, help="path to input image to be OCR'd")
    ap.add_argument("-p", "--preprocess", type=str, default="thresh", help="type of preprocessing to be done")
    return vars(ap.parse_args())


def show_image(*images):
    print(type(images))
    print(type(images[0]))
    cv2.imshow("Image", images[0])
    cv2.imshow("Output", images[1])
    cv2.waitKey(0)


if __name__ == '__main__':
    # retrieve parameters
    args = cmd_args(argparse.ArgumentParser())

    # generate pre-process the image
    if args is None:
        exit(1)
    image, gray = preprocess_image_with_filename(args["image"], args["preprocess"])

    # ocr by tesseract
    ocr_image(gray)

    # show the output images
    show_image(image, gray)
