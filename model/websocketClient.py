import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from model.transmissionImage import transmissionImage
from model.computerIO import computerIO
from socketIO_client import SocketIO, LoggingNamespace
import random

class websocketClient(object):
    def __init__(self, room_id=None):
        url = 'localhost'
        port = 5000
        self.socketIO = SocketIO(url, port, LoggingNamespace)
        self.computerIOModel = computerIO()
        self.transmissionImageModel = transmissionImage()
        self.room_id = room_id or self.getRandId()
        self.vote_id = None
        print("websocketClient is running url: %s, port: %s, room_id: %s" %(url, port, room_id))

    def emit(self, on_content, value=None):
        self.socketIO.emit(on_content, value)

    def getRoomId(self):
        return self.room_id
    
    def getRandId(self):
        return ''.join(["%s" % random.randint(0, 9) for num in range(6)])

    def createVote(self):
        self.vote_id = self.getRandId()

    def getVoteId(self):
        return self.vote_id

    def thread(self):
        def screenshop_requests(*args):
            print(args)
            image_content = self.transmissionImageModel.PILimageToBase64(
                self.computerIOModel.screenshop()
            )
            self.socketIO.emit('screenshop_revice', {
                "image": image_content, "user_id": args[0]["user_id"]
            })
        def rollCall_response(*args):
            print(args)
        while True:
            self.socketIO.on('screenshop_requests', screenshop_requests)
            self.socketIO.on('rollCall_response', rollCall_response)
            self.socketIO.wait(seconds=3)

    def send2Audience(self, room_id):
        image_content = self.transmissionImageModel.PILimageToBase64(
            self.computerIOModel.screenshop()
        )
        self.socketIO.emit('send2Audience', {"image": image_content, "room_id": room_id})