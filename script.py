from model.menu_processor import ocr_menu

if __name__ == "__main__":
    ocr_menu(data_dir="samples", filename='menu_en.pdf', data_set='devset')
