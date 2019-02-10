#!/usr/bin/python

import wx
import wx.lib.scrolledpanel
from PIL import Image

class setConfig(wx.Frame):
    def __init__(self, parent):
        super(setConfig, self).__init__(parent, title = "setConfig")
        self.Maximize(True)
        ### variable ###
        self.position_1_value = {"x": float(), "y": float()}
        self.position_2_value = {"x": float(), "y": float()}
        self.position_3_value = {"x": float(), "y": float()}
        self.position_4_value = {"x": float(), "y": float()}
        self.position_exchange_count = 0
        self.image_path = "../res/image.jpg"
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
        self.img = wx.Image(self.image_path, wx.BITMAP_TYPE_ANY)
        self.image_ctrl.SetBitmap(wx.BitmapFromImage(self.img))
        self.image_panel.Layout()
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
        # set hbox2
        self.hbox2 = wx.BoxSizer(wx.HORIZONTAL) 
        self.image_sizer.Add(self.hbox2 , 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
        # set position_3 text
        self.position_3 = wx.StaticText(self.image_panel, label = "左下座標")
        self.hbox2.Add(self.position_3, 2, wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5) 
        # set position_4 text
        self.position_4 = wx.StaticText(self.image_panel, label = "右下座標")
        self.hbox2.Add(self.position_4,1,wx.EXPAND|wx.ALIGN_LEFT|wx.ALL,5)
        # frame sizer
        self.frame_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.frame_sizer.Add(self.image_panel, proportion=1, flag=wx.EXPAND | wx.ALL)
        self.frame_panel.SetSizer(self.frame_sizer)

        ### logic ###
        self.image_ctrl.Bind(wx.EVT_LEFT_UP, self.ImageCtrlOnMouseClick)
        self.image_ctrl.Bind(wx.EVT_SIZE, self.windowResizeCallback)

        return

    def setWidthOffset(self):
        window_width, _ = self.GetSize()
        with Image.open(self.image_path) as img:
            image_width, _ = img.size
        return (window_width - image_width) / 2 - 10

    def windowResizeCallback(self, event):
        self.offset_width = self.setWidthOffset()

    def ImageCtrlOnMouseClick(self, event):
        ctrl_pos = event.GetPosition()
        pos = self.image_ctrl.ScreenToClient(ctrl_pos)
        screen_pos = self.frame_panel.GetScreenPosition()
        relative_pos_x = pos[0] + screen_pos[0] - self.offset_width
        relative_pos_y = pos[1] + screen_pos[1] - self.offset_height
        print("image postion ", relative_pos_x, relative_pos_y)
        if self.position_exchange_count == 0:
            self.position_1.SetLabel("左上座標 %s,%s" %(str(relative_pos_x),str(relative_pos_y)))
            self.position_1_value = {"x": relative_pos_x, "y": relative_pos_y}
        elif self.position_exchange_count == 1:
            self.position_2.SetLabel("右上座標 %s,%s" %(str(relative_pos_x),str(relative_pos_y)))
            self.position_2_value = {"x": relative_pos_x, "y": relative_pos_y}
        elif self.position_exchange_count == 2:
            self.position_3.SetLabel("左下座標 %s,%s" %(str(relative_pos_x),str(relative_pos_y)))
            self.position_3_value = {"x": relative_pos_x, "y": relative_pos_y}
        elif self.position_exchange_count == 3:
            self.position_4.SetLabel("右下座標 %s,%s" %(str(relative_pos_x),str(relative_pos_y)))
            self.position_4_value = {"x": relative_pos_x, "y": relative_pos_y}
        self.position_exchange_count = 0 if self.position_exchange_count >= 3 else self.position_exchange_count + 1

app = wx.PySimpleApp()
frame = setConfig(None)
frame.Show()
app.MainLoop()