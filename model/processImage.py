import cv2
import numpy as np

class processImage(object):
    def __init__(self):
        pass

    def perspective(self, frame, position_1, position_2, position_3, position_4, debug=False):
        cv2.circle(frame, position_1, 5, (0, 0, 255), -1)
        cv2.circle(frame, position_2, 5, (0, 0, 255), -1)
        cv2.circle(frame, position_3, 5, (0, 0, 255), -1)
        cv2.circle(frame, position_4, 5, (0, 0, 255), -1)
        height, width, _ = frame.shape
        pts1 = np.float32([position_1, position_2, position_3, position_4])
        pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])

        matrix = cv2.getPerspectiveTransform(pts1, pts2)
        result = cv2.warpPerspective(frame, matrix, (width, height))

        if debug == True:
            cv2.imshow("Frame", frame)
            cv2.imshow("Perspective transformation", result)

        return result
