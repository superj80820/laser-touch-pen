import matplotlib.pyplot as plt
from PIL import Image
import matplotlib.image as mpimg
import wx
import wx.lib.scrolledpanel

class discussFigure(object):
    def __init__(self):
        pass

    def vote(self, vote_item1, vote_item2):
        total_width, n = 0.8, 2
        width = total_width / n
        x = (total_width - width) / 2

        plt.bar(x, vote_item1["value"],  width=width, label=vote_item1["name"])
        plt.bar(x + width, vote_item2["value"], width=width, label=vote_item2["name"])
        plt.legend()
        plt.show()

    def rollCall(self, present, absent, late, excused):
        labels = ["present", "absent", "late", "excused"]
        sizes = [present["value"], absent["value"], late["value"], excused["value"]]
        explode = (0, 0.1, 0, 0) 

        plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
        plt.axis('equal') # Equal aspect ratio
        plt.show()

    def discussImage(self, image_path, word):
        class discussImageForm(wx.Frame):
            def __init__(self, parent, image_path, word):
                super(discussImageForm, self).__init__(parent, title = "討論", style=wx.DEFAULT_FRAME_STYLE, size=(300, 80))
                self.Maximize(True)
                ### variable ###

                ### layout ###
                self.panel = wx.Panel(self, wx.ID_ANY)
                mastersizer = wx.BoxSizer(wx.VERTICAL)
                self.image = wx.StaticBitmap(self.panel, -1, wx.Bitmap(image_path, wx.BITMAP_TYPE_ANY))
                self.class_number = wx.StaticText(self.panel, label = word)
                self.class_number.SetFont(wx.Font(30, wx.DECORATIVE, wx.NORMAL, wx.NORMAL))
                
                # Additional object
                mastersizer.Add(self.image, 1, wx.ALIGN_CENTRE_HORIZONTAL)
                mastersizer.Add(self.class_number, 1, wx.ALIGN_CENTRE_HORIZONTAL)
                self.panel.SetSizer(mastersizer)
                self.Centre()
                self.Show()

                ### logic ###

                return

        app = wx.PySimpleApp()
        class_number_window = discussImageForm(None, image_path, word)
        class_number_window.Show()
        app.MainLoop()

