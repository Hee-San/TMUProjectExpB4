# -*- coding: utf-8 -*-

def unNormalize(img):
    ans = img
    return ans

def sizeNormalize(img):
    # ここに書く
    ans = img
    return ans


def luminanceNormalize(img):
    # ここに書く
    ans = img
    return ans


def sizeAndLuminanceNnnormalize(img):
    ans1 = sizeNormalize(img)
    ans2 = luminanceNormalize(ans1)
    return ans2