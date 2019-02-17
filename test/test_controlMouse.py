import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from model.controlMouse import controlMouse
import unittest

class TestStringMethods(unittest.TestCase):
    def setUp(self):
        self.controlMouseObject = controlMouse()

    def test_click(self):
        print(self._testMethodName)
        self.controlMouseObject.click(0, 0)

    def test_refreshScreenSize(self):
        print(self._testMethodName)
        self.controlMouseObject.refreshScreenSize()

    def test_getScreenSize(self):
        print(self._testMethodName)
        width, hight = self.controlMouseObject.getScreenSize()
        self.assertIsInstance(width, int)
        self.assertIsInstance(hight, int)

if __name__ == '__main__':
    unittest.main()
