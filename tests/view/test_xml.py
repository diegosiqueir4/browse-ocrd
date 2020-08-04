import unittest
from unittest.mock import MagicMock
from ocrd_browser.view import ViewXml
from ocrd_browser.window import MainWindow

class XmlViewTestCase(unittest.TestCase):

    def setUp(self):
        self.vx = ViewXml('unique',MagicMock(spec=MainWindow))

    def test_can_construct(self):
        self.assertIsNotNone(self.vx)


if __name__ == '__main__':
    unittest.main()