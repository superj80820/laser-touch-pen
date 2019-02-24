import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from model.websocketClient import websocketClient
import time
import threading
import unittest


class TestStringMethods(unittest.TestCase):
    def setUp(self):
        self.websocketClientModel = websocketClient()

    def test_emit(self):
        print(self._testMethodName)
        self.websocketClientModel.emit("create_room", self.websocketClientModel.getRoomId())

    def test_thread(self):
        self.websocketClientModel.emit("create_room", self.websocketClientModel.getRoomId())
        self.websocketClientModel.thread()

if __name__ == '__main__':
    unittest.main()
