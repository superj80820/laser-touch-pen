#執行所需之插件  
colorsys  
os  
time  
numpy               1.14.5  
opencv-python       3.4.3.18  
Keras               2.2.4  
Keras-Applications  1.0.6  
Keras-Preprocessing 1.0.5  
tensorboard         1.8.0  
tensorflow          1.8.0  
Pillow              5.3.0
------------------------------  
#訓練時的須執行內容與順序  
wget https://pjreddie.com/media/files/yolov3.weights  
cd VOCdevkit/VOC2007  
python make_main_txt.py  
cd ../..  
python voc_annotation.py  
python convert.py -w yolov3.cfg yolov3.weights model_data/yolo_weights.h5  
python train.py  

----------------------------------------
#訓練
CUDA可看這個：https://zhuanlan.zhihu.com/p/38223869  
pip install numpy  
pip install opencv-python  
pip install Keras==2.2.4
pip install tensorflow-gpu==1.8.0  
pip install pillow  
先下載這個https://drive.google.com/open?id=1qALJtHL4B1PiBhtFdyQQaXLI_5qtvKH2 放置於model\yolo\VOCdvkit直接覆蓋VOC2007  
wget https://pjreddie.com/media/files/yolov3.weights  
cd VOCdevkit/VOC2007  
python make_main_txt.py  
cd ../..  
python voc_annotation.py  
python convert.py -w yolov3.cfg yolov3.weights model_data/yolo_weights.h5  
python train.py 
