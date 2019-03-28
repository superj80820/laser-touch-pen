# laser-touch-pen

想要投影幕或者電腦有觸控螢幕 但又沒錢買觸控系統嗎:cry: 你可以用本系統讓你只需花約500塊 螢幕就有觸控功能:sparkles:

# 硬體

| 硬體 | 價格 |
| -------- | -------- |
| <img src="https://i.imgur.com/H4CZ4Kg.jpg" width="100"><br>&ensp;&ensp;&nbsp;Webcam | 300~500 |
| <img src="https://i.imgur.com/8OK6oh5.jpg" width="100"><br>&emsp;&ensp;&nbsp;雷射筆 | 100~300 |

## 系統介紹

系統架構
<br>
<img src="https://github.com/superj80820/superj80820.github.io/blob/master/laser-touch-pen/laser-touch-pen-system.jpg" width="800">

實際展示
<br>
<img src="https://github.com/superj80820/superj80820.github.io/blob/master/laser-touch-pen/laser-touch-pen-demo.gif" width="800">

## 使用說明

<img src="https://i.imgur.com/qCchtMM.jpg" width="800">

進入form資料夾 運行

```
python main.py
```

點選Webcam的四個座標 然後選擇Perspecive進行透視變換

設定好二值化上下限 (建議 上限: 255, 下限:235)

再點選Set進行二值化

最後點選Start開始運行

## 搭配

* 如果想要搭配在會議/上課使用 可以配合以下 [line_discuss](https://github.com/superj80820/line_discuss)

## Reference
* [perspective-transformation](https://pysource.com/2018/02/14/perspective-transformation-opencv-3-4-with-python-3-tutorial-13/)
* [HandMovementTracking](https://github.com/akshaybahadur21/HandMovementTracking)
* [Keyboard layout](https://stackoverflow.com/questions/5154530/wxpython-nested-sizers-and-little-square-in-top-left-corner)
* [matplotlib](https://juejin.im/post/5b801d8de51d4538940024e5)
