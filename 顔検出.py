# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import cv2, matplotlib
import numpy as np
import matplotlib.pyplot as plt

# read an image
img = cv2.imread('/Users/takashi/_Codes/TMU/TMUProjectExpB4/dataset/DB/jpeg/077.jpg')
 
# show image format (basically a 3-d array of pixel color info, in BGR format)
print(img)

# convert image to RGB color for matplotlib
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
 
# show image with matplotlib
plt.imshow(img)

# カスケード分類器
cascade_path = '/Users/takashi/_Codes/TMU/TMUProjectExpB4/haarcascade_frontalface_default.xml'
cascade = cv2.CascadeClassifier(cascade_path)

facerect = cascade.detectMultiScale(img, scaleFactor=1.1, minNeighbors=2, minSize=(30,30))

color=(255,255,255)

if len(facerect) > 0:
    for rect in facerect:
        # v2.rectangle(img, tuple(rect[0:2]), tuple(rect[0:2]+rect[2:4]), color, thickness=2)
        imgFace = img[rect[1]:rect[1]+rect[3], rect[0]:rect[0]+rect[2]]
        plt.imshow(imgFace)
        
    
    
    