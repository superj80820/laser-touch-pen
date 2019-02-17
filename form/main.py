#!/usr/bin/python
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from model.processImage import processImage
from model.controlMouse import controlMouse
import wx
import wx.lib.scrolledpanel
from PIL import Image
import cv2
import re
import threading
import math

class setConfig(wx.Frame):
    def __init__(self, parent):
        super(setConfig, self).__init__(parent, title = "setConfig")
        self.Maximize(True)
        ### variable ###
        self.cap = cv2.VideoCapture(0)
        _, self.frame = self.cap.read()
        self.debug = False
        self.position_1_value = [float(), float()]
        self.position_2_value = [float(), float()]
        self.position_3_value = [float(), float()]
        self.position_4_value = [float(), float()]
        self.image_hight_value = int()
        self.image_low_value = int()
        self.position_exchange_count = 0
        self.image_path = "../res/test_main.jpg"
        self.offset_width = self.setWidthOffset()
        self.offset_height = 0

        ### layout ###
        # add a panel so it looks the correct on all platforms
        self.frame_panel = wx.Panel(self)
        # set image panel
        self.image_panel = wx.lib.scrolledpanel.ScrolledPanel(self.frame_panel, style=wx.SIMPLE_BORDER)
        self.image_panel.SetAutoLayout(True)
        self.image_panel.SetupScrolling()
        # set image
        self.image_ctrl = wx.StaticBitmap(self.image_panel)
        # set boxsizer
        self.image_sizer = wx.BoxSizer(wx.VERTICAL)
        # set preivew image
        self.image_sizer.Add(self.image_ctrl, 0, wx.EXPAND, 0)
        self.image_panel.SetSizer(self.image_sizer)
        # set hbox1
        self.hbox1 = wx.BoxSizer(wx.HORIZONTAL) 
        self.image_sizer.Add(self.hbox1 , 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
        # set position_1 text
        self.position_1 = wx.StaticText(self.image_panel, label = "左上座標")
        self.hbox1.Add(self.position_1, 2, wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5) 
        # set position_2 text
        self.position_2 = wx.StaticText(self.image_panel, label = "右上座標")
        self.hbox1.Add(self.position_2,1,wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5)
        # set text image hight
        self.image_hight = wx.TextCtrl(self.image_panel, -1, '0', size=(230, -1), style=wx.TE_RIGHT | wx.TE_PROCESS_ENTER) 
        self.hbox1.Add(self.image_hight,1,wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5)
        # set hbox2
        self.hbox2 = wx.BoxSizer(wx.HORIZONTAL) 
        self.image_sizer.Add(self.hbox2 , 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
        # set position_3 text
        self.position_3 = wx.StaticText(self.image_panel, label = "左下座標")
        self.hbox2.Add(self.position_3, 2, wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5) 
        # set position_4 text
        self.position_4 = wx.StaticText(self.image_panel, label = "右下座標")
        self.hbox2.Add(self.position_4,1,wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5)
        # set text image low
        self.image_low = wx.TextCtrl(self.image_panel, -1, '0', size=(230, -1), style=wx.TE_RIGHT | wx.TE_PROCESS_ENTER) 
        self.hbox2.Add(self.image_low,1,wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5)
        # set buttom refresh
        self.buttom_refresh = wx.ToggleButton(self.image_panel, -1, "Refresh")
        self.image_sizer.Add(self.buttom_refresh, 0, wx.EXPAND|wx.ALIGN_CENTER)
        # set buttom set image
        self.buttom_set_image = wx.ToggleButton(self.image_panel, -1, "Set")
        self.image_sizer.Add(self.buttom_set_image, 0, wx.EXPAND|wx.ALIGN_CENTER)
        # set buttom start
        self.buttom_start = wx.ToggleButton(self.image_panel, -1, "Start")
        self.image_sizer.Add(self.buttom_start, 0, wx.EXPAND|wx.ALIGN_CENTER)
        # frame sizer
        self.frame_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.frame_sizer.Add(self.image_panel, proportion=1, flag=wx.EXPAND | wx.ALL)
        self.frame_panel.SetSizer(self.frame_sizer)

        ### logic ###
        self.showImage()
        self.image_ctrl.Bind(wx.EVT_LEFT_UP, self.ImageCtrlOnMouseClick)
        self.image_ctrl.Bind(wx.EVT_SIZE, self.windowResizeCallback)
        self.buttom_refresh.Bind(wx.EVT_LEFT_UP, self.showRefresh)
        self.buttom_set_image.Bind(wx.EVT_LEFT_UP, self.showSetImage)
        self.image_hight.Bind(wx.EVT_KEY_UP, self.setImageHight)
        self.image_low.Bind(wx.EVT_KEY_UP, self.setImageLow)
        self.buttom_start.Bind(wx.EVT_LEFT_UP, self.startTracker)

        return

    def setImageHight(self, event):
        value = self.image_hight.GetValue()
        if re.search('\d+', value) != None:
            self.image_hight_value = int(value)
        else:
            self.image_hight_value = 0
        print("hight", self.image_hight_value)

    def setImageLow(self, event):
        value = self.image_low.GetValue()
        if re.search('\d+', value) != None:
            self.image_low_value = int(value)
        else:
            self.image_low_value = 0
        print(self.image_low_value)

    def showRefresh(self, event):
        self.getNewImage()
        self.showImage()

    def showSetImage(self, event):
        self.setFrame(self.tracker())
        self.setPreviewImage()
        self.showImage()

    def setPreviewImage(self):
        self.frame = processImageObject.getSetPreviewImage(self.frame)

    def setFrame(self, frame):
        self.frame = frame

    def getNewImage(self):
        _, self.frame = self.cap.read()

    def showImage(self):
        height,width = self.frame.shape[:2]
        image = wx.Bitmap.FromBuffer(width, height, self.BGR_to_RGB(self.frame))
        self.image_ctrl.SetBitmap(image)
        self.image_panel.Layout()

    def BGR_to_RGB(self, image):
        (B,G,R) = cv2.split(image)
        image=cv2.merge([R,G,B])
        return image

    def setWidthOffset(self):
        window_width, _ = self.GetSize()
        _, image_width, _ = self.frame.shape
        return (window_width - image_width) / 2 - 10

    def windowResizeCallback(self, event):
        self.offset_width = self.setWidthOffset()

    def ImageCtrlOnMouseClick(self, event):
        ctrl_pos = event.GetPosition()
        pos = self.image_ctrl.ScreenToClient(ctrl_pos)
        screen_pos = self.frame_panel.GetScreenPosition()
        relative_pos_x = int(pos[0] + screen_pos[0] - self.offset_width)
        relative_pos_y = int(pos[1] + screen_pos[1] - self.offset_height)
        print("image postion ", relative_pos_x, relative_pos_y)
        if self.position_exchange_count == 0:
            self.position_1.SetLabel("左上座標 %s,%s" %(str(relative_pos_x),str(relative_pos_y)))
            self.position_1_value = [relative_pos_x, relative_pos_y]
        elif self.position_exchange_count == 1:
            self.position_2.SetLabel("右上座標 %s,%s" %(str(relative_pos_x),str(relative_pos_y)))
            self.position_2_value = [relative_pos_x, relative_pos_y]
        elif self.position_exchange_count == 2:
            self.position_3.SetLabel("左下座標 %s,%s" %(str(relative_pos_x),str(relative_pos_y)))
            self.position_3_value = [relative_pos_x, relative_pos_y]
        elif self.position_exchange_count == 3:
            self.position_4.SetLabel("右下座標 %s,%s" %(str(relative_pos_x),str(relative_pos_y)))
            self.position_4_value = [relative_pos_x, relative_pos_y]
        self.position_exchange_count = 0 if self.position_exchange_count >= 3 else self.position_exchange_count + 1

    def tracker(self):
        self.center, frame = processImageObject.controllerTracker(
            frame=self.frame,
            position_1=tuple(self.position_1_value),
            position_2=tuple(self.position_2_value),
            position_3=tuple(self.position_3_value),
            position_4=tuple(self.position_4_value),
            low=self.image_low_value,
            hight=self.image_hight_value,
            debug = self.debug
        )
        return frame

    def trackerControlMouse(self):
        while True:
            self.getNewImage()
            self.tracker()
            print(self.center)
            controlMouseObject.click(self.center)

    def startTracker(self, event):
        t = threading.Thread(target = self.trackerControlMouse)
        t.start()

if __name__ == '__main__':
    processImageObject = processImage()
    controlMouseObject = controlMouse()

    app = wx.PySimpleApp()
    window = setConfig(None)
    window.Show()
    app.MainLoop()