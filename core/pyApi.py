import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import json
from model.handDetection import handDetection

def callPython(object, func):
    """
    reference: https://stackoverflow.com/questions/3061/calling-a-function-of-a-module-by-using-its-name-a-string
    """
    return getattr(globals()[object], func)()

if __name__ == '__main__':
    handDetectionModel = handDetection("./../res/image.jpg")

    object = str(sys.argv[1])
    func = str(sys.argv[2])
    sys.stdout.write(str(callPython(object, func)))