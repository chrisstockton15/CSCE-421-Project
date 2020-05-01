# -*- coding: utf-8 -*-
#Glasses_Detection.ipynb

#Automatically generated by Colaboratory.


# define helper functions
def imShow(path):
  import cv2
  import matplotlib.pyplot as plt



# Remove comments to run untraimed detection on sample images seen in report

# run untrained darknet detection for sample image 1
# !./darknet detect cfg/yolov3.cfg yolov3.weights data/glasses001.jpg
# imShow('predictions.jpg')

# run untrtained darknet detection for sample image 2
# !./darknet detect cfg/yolov3.cfg yolov3.weights data/glasses002.jpg
# imShow('predictions.jpg')

# run untrtained darknet detection for sample image 2
# !./darknet detect cfg/yolov3.cfg yolov3.weights data/glasses002.jpg
# imShow('predictions.jpg')


# BEGIN TRAINING -dont_show flag stops chart displaying (can crash Google Colab)
!./darknet detector train data/obj.data cfg/yolov3-custom.cfg darknet53.conv.74 -dont_show

# resume training from saved backup in case something crashed
#!./darknet detector train data/obj.data cfg/yolov3_custom.cfg /mydrive/yolov3/backup/yolov3_custom_last.weights -dont_show


# go into cfg folder to set custom cfg to test mode 
 %cd cfg
!sed -i 's/batch=64/batch=1/' yolov3-custom.cfg
!sed -i 's/subdivisions=16/subdivisions=1/' yolov3-custom.cfg
 %cd ..

# run your custom detector with this command (upload an image to your google drive to test, thresh flag sets accuracy that detection must be in order to show it)
!./darknet detector test data/obj.data cfg/yolov3-custom.cfg backup/yolov3-custom_last.weights data/glasses006.jpg -thresh 0.3
imShow('predictions.jpg')

