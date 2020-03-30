from pathlib import Path

from pdf2image import convert_from_path

from model.image_processor import preprocess_image


def convert_pdf_to_images(menu_path, filename):
    menu_images_path = menu_path + "/" + filename[:-4]
    Path(menu_images_path).mkdir(parents=True, exist_ok=True)

    # convert pdf menu into images
    images_from_path = convert_from_path(menu_path + "/" + filename)

    # save images to specified folder
    file_index = 0
    for image_from_path in images_from_path:
        print(image_from_path.filename)
        file_index += 1
        try:
            convert_image_filename = menu_images_path + "/" + filename[:-4] + "_" + str(file_index) + ".png"
            image_from_path.save(convert_image_filename)
        except IOError:
            print("cannot create thumbnail for", convert_image_filename)
    return images_from_path


def ocr(data_dir="samples", filename='menu_en.pdf', data_set='devset'):
    menu_path = data_dir + "/" + data_set

    # convert pdf into menu png images
    menu_images = convert_pdf_to_images(menu_path, filename)

    # pre-process images
    image, gray, gray_filename = preprocess_image(args["image"], args["preprocess"])

