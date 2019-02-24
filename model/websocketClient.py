import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from model.transmissionImage import transmissionImage
from model.computerIO import computerIO
from socketIO_client import SocketIO, LoggingNamespace
import random

class websocketClient(object):
    def __init__(self, room_id=None):
        self.socketIO = SocketIO('localhost', 5000, LoggingNamespace)
        self.computerIOModel = computerIO()
        self.transmissionImageModel = transmissionImage()
        if room_id == None: self.room_id = ''.join(["%s" % random.randint(0, 9) for num in range(6)])

    def emit(self, on_content, value=None):
        self.socketIO.emit(on_content, value)

    def getRoomId(self):
        return self.room_id

    def thread(self):
        def screenshop_requests(*args):
            print(args)
            image_content = self.transmissionImageModel.PILimageToBase64(
                self.computerIOModel.screenshop()
            )
            self.socketIO.emit('screenshop_revice', {
                "image": image_content, "user_id": args[0]["user_id"]
            })
        while True:
            self.socketIO.on('screenshop_requests', screenshop_requests)
            self.socketIO.wait(seconds=3)