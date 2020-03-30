from unittest import TestCase

from model.menu_processor import ocr, convert_pdf_to_images


class MenuProcessorTest(TestCase):

    # def test_ocr(self):
    #     ocr(data_dir="../samples")
    #     self.assertEqual("a", "a")

    def test_convert_pdf_to_images(self):
        menu_images = convert_pdf_to_images("../samples/devset", "menu_mix_en_cn.pdf")
        self.assertEqual(len(menu_images), 2)
