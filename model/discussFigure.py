import matplotlib.pyplot as plt
from PIL import Image
import matplotlib.image as mpimg

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

    def discussImage(self, image_path):
        figManager = plt.get_current_fig_manager()
        figManager.window.showMaximized()
        img = mpimg.imread(image_path)
        plt.imshow(img)