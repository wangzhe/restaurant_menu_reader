from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError
)
from pdf2image import convert_from_path, convert_from_bytes

import tempfile


def ocr(filename):
    # convert pdf menu into images
    with tempfile.TemporaryDirectory() as path:
        images_from_path = convert_from_path('../samples/devset/menu_en.pdf', output_folder=path)
        for image_from_path in images_from_path:
            print(image_from_path.filename)
        # Do something here
