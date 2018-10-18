#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2
import os

import faceTrimming as ft

path = os.getcwd()
DB_path = path + '/dataset/DB/jpeg/'
output_path = path + '/dataset/DBface/jpeg/'

nDB = 200

# outputファイルが無ければ作成
if not os.path.exists(output_path):
    os.mkdir(output_path)



for i in range(1,nDB):
    # read an image
    img = cv2.imread(DB_path + '%03d' % i + '.jpg')
    faces = ft.faceTrimming(img, path)
    for j in range(len(faces)):
        output = output_path + '%03d' % i + '_' + '%02d' % j + '.jpg'
        cv2.imwrite(output, faces[j])


