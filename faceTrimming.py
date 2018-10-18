# -*- coding: utf-8 -*-
import cv2

def faceTrimming(img, path):
    cascade_path = path + '/haarcascade_frontalface_default.xml'
    # カスケード分類器
    cascade = cv2.CascadeClassifier(cascade_path)
    facerect = cascade.detectMultiScale(img, scaleFactor=1.1, minNeighbors=2, minSize=(100,100))
    ans = []
    for index, rect in enumerate(facerect):
        imgFace = img[rect[1]:rect[1]+rect[3], rect[0]:rect[0]+rect[2]]
        ans.append(imgFace)
    return ans