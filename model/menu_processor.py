from pathlib import Path

from PIL import Image
from pdf2image import convert_from_path

from model.image_processor import ocr_image


def convert_pdf_to_images(menu_path, filename):
    menu_images_path = menu_path + "/" + filename[:-4]
    Path(menu_images_path).mkdir(parents=True, exist_ok=True)
    print(menu_path + "/" + filename)

    # convert pdf menu into images
    if filename[-3:].lower() == "pdf":
        images_from_path = convert_from_path(menu_path + "/" + filename)
    else:
        images_from_path = [Image.open(menu_path + "/" + filename)]

    # save images to specified folder
    for file_index, image_from_path in enumerate(images_from_path):
        try:
            convert_image_filename = menu_images_path + "/" + filename[:-4] + "_" + str(file_index) + ".png"
            image_from_path.save(convert_image_filename)
        except IOError:
            print("cannot create image", convert_image_filename)
    return images_from_path


def ocr_menu(data_dir="samples", filename='menu_en.pdf', data_set='devset'):
    menu_path = data_dir + "/" + data_set

    # convert pdf into menu PIL images
    menu_images = convert_pdf_to_images(menu_path, filename)

    for menu_page_image in menu_images:
        menu_text = ocr_image(menu_page_image)
        print(menu_text)


if __name__ == "__main__":
    print("filename"[:-3].lower())
