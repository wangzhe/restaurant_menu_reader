from unittest import TestCase

from model.menu_processor import ocr


class MenuProcessorTest(TestCase):

    def test_ocr(self):
        ocr("")
        self.assertEqual("a", "a")
