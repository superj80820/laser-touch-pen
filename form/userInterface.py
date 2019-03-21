#!/usr/bin/python
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from model.websocketClient import websocketClient
from model.discussFigure import discussFigure
from model.transmissionImage import transmissionImage
import threading
import wx
import wx.lib.scrolledpanel

class keybaord(wx.Frame):
    def __init__(self, parent):
        super(keybaord, self).__init__(parent, title = "keybaord", style=wx.DEFAULT_FRAME_STYLE | wx.STAY_ON_TOP, size=(420, 290))
        ### variable ###
        self.transmissionImageModel = transmissionImage()
        self.websocketClientModel = websocketClient("123456")
        self.discussFigureModel = discussFigure()
        self.websocketClientModel.emit("create_room", self.websocketClientModel.getRoomId())
        t = threading.Thread(target = self.websocketClientModel.thread)
        t.start()

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
        btn_1_e = wx.Button(self.panel, id=5, label='結束', size=(80, 80))
        btn_2_a = wx.Button(self.panel, id=6, label='a', size=(80, 80))
        btn_2_b = wx.Button(self.panel, id=7, label='b', size=(80, 80))
        btn_2_c = wx.Button(self.panel, id=8, label='c', size=(80, 80))
        btn_2_d = wx.Button(self.panel, id=9, label='d', size=(80, 80))
        btn_2_e = wx.Button(self.panel, id=10, label='d', size=(80, 80))
        btn_3_a = wx.Button(self.panel, id=11, label='發作業', size=(80, 80))
        btn_3_b = wx.Button(self.panel, id=12, label='點名', size=(80, 80))
        btn_3_c = wx.Button(self.panel, id=13, label='投票開始', size=(80, 80))
        btn_3_d = wx.Button(self.panel, id=14, label='投票結束', size=(80, 80))
        btn_3_e = wx.Button(self.panel, id=15, label='討論', size=(80, 80))
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
        def send2Audience(event, room_id=self.websocketClientModel.getRoomId()):
            t = threading.Thread(target = self.websocketClientModel.send2Audience, args=(room_id,))
            t.start()

        def rollCall(event):
            self.websocketClientModel.rollCall()
            resp = self.websocketClientModel.waitRollCallTrigger()
            with open("roll_call.txt", "w") as f:
                for item in resp[0]["members"]:
                    f.write(item)
            present = {"name": "present", "value": resp[0]["arrive_members"]}
            late = {"name": "late", "value": resp[0]["not_arrive_members"]}
            self.discussFigureModel.rollCall(present, late)

        def voteStar(event):
            self.websocketClientModel.createVote()
            self.websocketClientModel.voteStar()

        def voteEnd(envet):
            self.websocketClientModel.voteStop()
            resp = self.websocketClientModel.waitVoteStopTrigger()
            print("asdf%s"%resp)
            self.discussFigureModel.vote({"name":"O","value": int(resp[0][0]["item1"])}, {"name":"X","value": int(resp[0][1]["item2"])})

        def discussImage(event):
            self.websocketClientModel.discussImage()
            resp = self.websocketClientModel.waitDiscussImageTrigger()
            self.transmissionImageModel.base64ToImage(resp[0])
            self.discussFigureModel.discussImage("../res/imageToSave.jpg", resp[1])

        def clientThreadStop(event):
            self.websocketClientModel.threadStop()

        btn_1_e.Bind(wx.EVT_LEFT_DOWN, clientThreadStop)
        btn_3_a.Bind(wx.EVT_LEFT_DOWN, send2Audience)
        btn_3_b.Bind(wx.EVT_LEFT_DOWN, rollCall)
        btn_3_c.Bind(wx.EVT_LEFT_DOWN, voteStar)
        btn_3_d.Bind(wx.EVT_LEFT_DOWN, voteEnd)
        btn_3_e.Bind(wx.EVT_LEFT_DOWN, discussImage)

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