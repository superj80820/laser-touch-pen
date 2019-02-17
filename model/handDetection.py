import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '.'))
from yolo.yolo import first_run as yolo_set
from yolo.yolo import decect_mydata as yolo_run

class handDetection(object):
    def __init__(self, image_path):
        self.image_path = image_path

    def detection(self):
        yolo_set()
        outPut=yolo_run('model/yolo/testImgPlace/img.jpg')
        #測試時使用yolo內部我放置的刀子圖片，訓練完成後將修改為self
        yoloResult=outPut[0]
        return yoloResult
        #yolo辨識到的物品:OutPut[0]
        #yolo辨識到物品中間X值:OutPut[1]
        #yolo辨識到物品中間Y值:OutPut[2]
        # """
        # 如果偵測到手 請回傳手的類型
        # 如果沒有偵測到 請回傳False
        # """