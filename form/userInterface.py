#!/usr/bin/python
import wx
import wx.lib.scrolledpanel

class keybaord(wx.Frame):
    def __init__(self, parent):
        super(keybaord, self).__init__(parent, title = "keybaord", style=wx.DEFAULT_FRAME_STYLE | wx.STAY_ON_TOP, size=(420, 290))
        ### variable ###

        ### layout ###
        self.panel = wx.Panel(self, wx.ID_ANY)
        mastersizer = wx.BoxSizer(wx.VERTICAL)
        btnsizer_1 = wx.BoxSizer(wx.HORIZONTAL)
        btnsizer_2 = wx.BoxSizer(wx.HORIZONTAL)
        btnsizer_3 = wx.BoxSizer(wx.HORIZONTAL)
        btn_1_a = wx.Button(self.panel, id=1, label='a', size=(80, 80))
        btn_1_b = wx.Button(self.panel, id=2, label='b', size=(80, 80))
        btn_1_c = wx.Button(self.panel, id=3, label='c', size=(80, 80))
        btn_1_d = wx.Button(self.panel, id=4, label='d', size=(80, 80))
        btn_1_e = wx.Button(self.panel, id=5, label='d', size=(80, 80))
        btn_2_a = wx.Button(self.panel, id=6, label='a', size=(80, 80))
        btn_2_b = wx.Button(self.panel, id=7, label='b', size=(80, 80))
        btn_2_c = wx.Button(self.panel, id=8, label='c', size=(80, 80))
        btn_2_d = wx.Button(self.panel, id=9, label='d', size=(80, 80))
        btn_2_e = wx.Button(self.panel, id=10, label='d', size=(80, 80))
        btn_3_a = wx.Button(self.panel, id=11, label='a', size=(80, 80))
        btn_3_b = wx.Button(self.panel, id=12, label='b', size=(80, 80))
        btn_3_c = wx.Button(self.panel, id=13, label='c', size=(80, 80))
        btn_3_d = wx.Button(self.panel, id=14, label='d', size=(80, 80))
        btn_3_e = wx.Button(self.panel, id=15, label='d', size=(80, 80))
        # Additional object
        btnsizer_1.Add(btn_1_a, 0)
        btnsizer_1.Add(btn_1_b, 0)
        btnsizer_1.Add(btn_1_c, 0)
        btnsizer_1.Add(btn_1_d, 0)
        btnsizer_1.Add(btn_1_e, 0)
        btnsizer_2.Add(btn_2_a, 0)
        btnsizer_2.Add(btn_2_b, 0)
        btnsizer_2.Add(btn_2_c, 0)
        btnsizer_2.Add(btn_2_d, 0)
        btnsizer_2.Add(btn_2_e, 0)
        btnsizer_3.Add(btn_3_a, 0)
        btnsizer_3.Add(btn_3_b, 0)
        btnsizer_3.Add(btn_3_c, 0)
        btnsizer_3.Add(btn_3_d, 0)
        btnsizer_3.Add(btn_3_e, 0)
        mastersizer.Add(btnsizer_1, 1, wx.EXPAND)
        mastersizer.Add(btnsizer_2, 1, wx.EXPAND)
        mastersizer.Add(btnsizer_3, 1, wx.EXPAND)
        self.panel.SetSizer(mastersizer)
        self.Centre()
        self.Show()

        ### logic ###

        return

class classNumber(wx.Frame):
    def __init__(self, parent):
        super(classNumber, self).__init__(parent, title = "class number", style=wx.DEFAULT_FRAME_STYLE | wx.STAY_ON_TOP, size=(300, 80))
        ### variable ###

        ### layout ###
        self.panel = wx.Panel(self, wx.ID_ANY)
        mastersizer = wx.BoxSizer(wx.VERTICAL)
        self.class_number = wx.StaticText(self.panel, label = "課程代碼 %s" %self.getClassNumber())
        self.class_number.SetFont(wx.Font(30, wx.DECORATIVE, wx.NORMAL, wx.NORMAL))
        
        # Additional object
        mastersizer.Add(self.class_number, 1, wx.ALIGN_CENTRE_HORIZONTAL)
        self.panel.SetSizer(mastersizer)
        self.Centre()
        self.Show()

        ### logic ###

        return

    def getClassNumber(self):
        return str(12345)

def showOnScreenRightButtom(window):
    dw, dh = wx.DisplaySize()
    w, h = window.GetSize()
    x = dw - w
    y = dh - h
    window.SetPosition((x, y))

def showAlignWindow(main_window ,align_window):
    dw, dh = wx.DisplaySize()
    mw, mh = main_window.GetSize()
    aw, _ = align_window.GetSize()
    x = dw - aw - mw
    y = dh - mh
    main_window.SetPosition((x, y))

if __name__ == '__main__':
    app = wx.PySimpleApp()
    keybaord_window = keybaord(None)
    class_number_window = classNumber(None)
    showOnScreenRightButtom(keybaord_window)
    showAlignWindow(class_number_window, keybaord_window)
    keybaord_window.Show()
    class_number_window.Show()
    app.MainLoop()