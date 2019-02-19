import cv2
import numpy as np
from collections import deque
import win32api

class processImage(object):
    def __init__(self):
        self.width = win32api.GetSystemMetrics(0)
        self.hight = win32api.GetSystemMetrics(1)
        lower_upper = {
            "green": {"lower": [110, 50, 50], "upper": [130, 255, 255]},
            "puple": {"lower": [300, 62, 46], "upper": [326, 93, 99]},
            "yello": {"lower": [40, 50, 50], "upper": [60, 0, 255]},
            "red": {"lower": [ 80,  0, 214]   , "upper": [100,  16, 255]  },
            "white": {"lower": [140, 0, 215], "upper": [160, 14, 295]}
        }
        self.Lower = np.array(lower_upper["red"]["lower"])
        self.Upper = np.array(lower_upper["red"]["upper"])
        self.pts = deque(maxlen=5)

    def controllerTracker(self, *args, **kwargs):
        debug = False if kwargs.get("debug") in [None, False] else True
        frame = self.perspective(kwargs["frame"], kwargs["position_1"], kwargs["position_2"], kwargs["position_3"], kwargs["position_4"], debug=debug)
        frame = self.laserTracking(frame, low=kwargs.get("low"), hight=kwargs.get("hight"), debug=debug)
        return frame

    def refreshScreenSize(self):
        self.width = win32api.GetSystemMetrics(0)
        self.hight = win32api.GetSystemMetrics(1)

    def getScreenSize(self):
        return self.width, self.hight

    def perspective(self, frame, position_1, position_2, position_3, position_4, debug=False):
        height, width, _ = frame.shape
        pts1 = np.float32([position_1, position_2, position_3, position_4])
        pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])

        matrix = cv2.getPerspectiveTransform(pts1, pts2)
        result = cv2.warpPerspective(frame, matrix, (width, height))

        if debug == True:
            cv2.circle(frame, position_1, 5, (0, 0, 255), -1)
            cv2.circle(frame, position_2, 5, (0, 0, 255), -1)
            cv2.circle(frame, position_3, 5, (0, 0, 255), -1)
            cv2.circle(frame, position_4, 5, (0, 0, 255), -1)

            cv2.imshow("Frame", frame)
            cv2.imshow("Perspective transformation", result)

        return result

    def laserTracking(self, frame, ones=1, low=200, hight=255,debug=False):
        frame = cv2.resize(frame, (self.width, self.hight))
        color_mode=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        kernel=np.ones((ones, ones),np.uint8)
        mask=cv2.inRange(color_mode, low, hight)
        mask = cv2.erode(mask, kernel, iterations=2)
        mask=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel)
        #mask=cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernel)
        mask = cv2.dilate(mask, kernel, iterations=1)
        res=cv2.bitwise_and(frame,frame,mask=mask)
        cnts,heir=cv2.findContours(mask.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[-2:]
        center = None
        if len(cnts) > 0:
            c = max(cnts, key=cv2.contourArea)
            ((x, y), radius) = cv2.minEnclosingCircle(c)
            M = cv2.moments(c)
            if M["m00"] != 0:
                center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
            else: # Edge screen case
                center = (self.width, self.hight)
        else:
            center = None

        if debug == True:
            if len(cnts) > 0:
                if radius > 5:
                    cv2.circle(frame, (int(x), int(y)), int(radius),(0, 255, 255), 2)
                    cv2.circle(frame, center, 5, (0, 0, 255), -1)

            self.pts.appendleft(center)
            for i in range (1,len(self.pts)):
                if self.pts[i-1]is None or self.pts[i] is None:
                    continue
                thick = int(np.sqrt(len(self.pts) / float(i + 1)) * 2.5)
                cv2.line(frame, self.pts[i-1],self.pts[i],(0,0,225),thick)

            cv2.imshow("color_mode", color_mode)
            cv2.imshow("Frame", frame)
            cv2.imshow("mask",mask)
            cv2.imshow("res",res)
        return center, res

    def getSetPreviewImage(self, frame):
        return cv2.resize(frame, (600, 480)) 