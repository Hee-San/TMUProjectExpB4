# -*- coding: utf-8 -*-

import cv2

def faceTrimming(img, cascade, name, output_path):
    facerect = cascade.detectMultiScale(img, scaleFactor=1.1, minNeighbors=2, minSize=(100,100))
    if len(facerect) > 0:
        for index, rect in enumerate(facerect):
            output = output_path + '%03d' % name + '_' + '%02d' % index + '.jpg'
            # v2.rectangle(img, tuple(rect[0:2]), tuple(rect[0:2]+rect[2:4]), color, thickness=2)
            imgFace = img[rect[1]:rect[1]+rect[3], rect[0]:rect[0]+rect[2]]
            # plt.imshow(imgFace)
            
            #認識結果の保存
            cv2.imwrite(output, imgFace)