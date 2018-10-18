# -*- coding: utf-8 -*-

import cv2, matplotlib
import numpy as np
import matplotlib.pyplot as plt
import os

path = os.getcwd()
DB_path = path + '/dataset/DB/jpeg/'
output_path = path + '/dataset/DBface/jpeg/'
cascade_path = path + '/haarcascade_frontalface_default.xml'

nDB = 200

# outputファイルが無ければ作成
if not os.path.exists(output_path):
    os.mkdir(output_path)


# カスケード分類器
cascade = cv2.CascadeClassifier(cascade_path)

for i in range(1,nDB):
    # read an image
    img = cv2.imread(DB_path + '%03d' % i + '.jpg')
    facerect = cascade.detectMultiScale(img, scaleFactor=1.1, minNeighbors=2, minSize=(100,100))

    if len(facerect) > 0:
        for index, rect in enumerate(facerect):
            output = output_path + '%03d' % i + '_' + '%02d' % index + '.jpg'
            # v2.rectangle(img, tuple(rect[0:2]), tuple(rect[0:2]+rect[2:4]), color, thickness=2)
            imgFace = img[rect[1]:rect[1]+rect[3], rect[0]:rect[0]+rect[2]]
            # plt.imshow(imgFace)
            
            #認識結果の保存
            cv2.imwrite(output, imgFace)