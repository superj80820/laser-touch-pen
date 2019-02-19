import win32api, win32con, win32gui
from collections import deque
import time
import threading

class controlMouse(object):
    def __init__(self):
        """
        if click: True
        elif not click: False
        """
        self.left_click_flag = False
        self.long_click = [int(), int()]
        self.long_click_offset = 100
        self.trigger_long_click_count = int()
        self.click_flag = "left"
        self.laser_flag = False
        self.long_click_flag = True
        t = threading.Thread(target = self.triggerLongClickCallback)
        t.start()

    def click(self, center, debug=False):
        if center != None:
            self.laser_flag = True
            win32api.SetCursorPos(center)
            if self.click_flag == "left" and self.left_click_flag == False:
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, center[0], center[1], 0, 0)
                self.left_click_flag = True
            elif self.click_flag == "right":
                win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, center[0], center[1], 0, 0)
                win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, center[0], center[1], 0, 0)
                self.click_flag = "left"
        else: # release click
            self.laser_flag = False
            if self.left_click_flag == True:
                _, _, (x, y) = win32gui.GetCursorInfo()
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)
                self.left_click_flag = False
                self.long_click_flag = True

    def triggerLongClickCallback(self):
        while True:
            _, _, (x, y) = win32gui.GetCursorInfo()
            print(x, y)
            print("click", self.click_flag)
            print("long", self.long_click_flag)
            if self.click_flag == "left" and self.laser_flag == True and self.long_click_flag == True:
                if abs(self.long_click[0] - x) < self.long_click_offset and abs(self.long_click[1] - y) < self.long_click_offset:
                    self.trigger_long_click_count += 1
                else:
                    self.long_click_flag = False
                    self.trigger_long_click_count = 0
                self.long_click = [x, y]
                if self.trigger_long_click_count >= 4:
                    self.click_flag = "right"
                    self.trigger_long_click_count = 0
            time.sleep(0.5)