import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from model.handDetection import handDetection
import unittest

class TestStringMethods(unittest.TestCase):
    def setUp(self):
        self.handDetectionModel = handDetection("./../res/image.jpg")

    def test_detection(self):
        print(self._testMethodName)
        self.assertTrue(self.handDetectionModel.detection())

if __name__ == '__main__':
    unittest.main()
