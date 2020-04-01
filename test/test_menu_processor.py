from unittest import TestCase

from model.menu_processor import ocr_menu, convert_pdf_to_images


class MenuProcessorTest(TestCase):

    def test_ocr(self):
        ocr_menu(data_dir="../samples", filename='menu_en.pdf', data_set='devset')
        self.assertEqual("a", "a")

    def test_convert_pdf_to_images_when_image_is_pdf(self):
        menu_images = convert_pdf_to_images("test_samples", "menu_pdf_test.pdf")
        self.assertEqual(len(menu_images), 1)
        print("A")

    def test_convert_pdf_to_images_when_image_is_jpg(self):
        menu_images = convert_pdf_to_images("test_samples", "menu_jpg_test.jpg")
        self.assertEqual(len(menu_images), 1)
        print("B")


