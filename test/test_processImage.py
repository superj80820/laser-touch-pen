import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from model.processImage import processImage
import cv2

if __name__ == "__main__":
    processImageObject = processImage()

    cap = cv2.VideoCapture(0)
    while True:
        _, frame = cap.read()
        processImageObject.perspective(frame, (155, 120), (480, 120), (20, 475), (620, 475), debug=True)
        key = cv2.waitKey(1)
        if key == 27:
            break
    cap.release()
    cv2.destroyAllWindows()