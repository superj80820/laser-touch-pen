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
------------------------------  
#訓練時的須執行內容與順序  
wget https://pjreddie.com/media/files/yolov3.weights  
cd VOCdevkit/VOC2007  
python make_main_txt.py  
cd ../..  
python voc_annotation.py  
python convert.py -w yolov3.cfg yolov3.weights model_data/yolo_weights.h5  
python train.py  