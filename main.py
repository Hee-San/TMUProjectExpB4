#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2, matplotlib
import numpy as np
import matplotlib.pyplot as plt
import os

import faceTrimming as ft

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
    ft.faceTrimming(img, cascade, i, output_path)

