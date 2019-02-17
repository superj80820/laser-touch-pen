import win32api, win32con, win32gui
from collections import deque

class controlMouse(object):
    def __init__(self):
        pass

    def click(self, center, debug=False):
        if center != None:
            win32api.SetCursorPos(center)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, center[0], center[1], 0, 0)
        else:
            _, _, (x,y) = win32gui.GetCursorInfo()
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)
