import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from model.processImage import processImage
import cv2

def connetWebcam(func, *args):
    cap = cv2.VideoCapture(0)
    while True:
        _, frame = cap.read()
        func(frame, *args, debug=True)
        key = cv2.waitKey(1)
        if key == 27:
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    processImageObject = processImage()
    # connetWebcam(processImageObject.perspective,(155, 120), (480, 120), (20, 475), (620, 475))
    connetWebcam(processImageObject.laserTracking, 200, 255)
    # connetWebcam(processImageObject.controllerTracker,(155, 120), (480, 120), (20, 475), (620, 475))