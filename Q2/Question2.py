#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import cv2
src="/Users/tom/Downloads/OpenCV_homework/Test_images/" 
names=["Lenna.png","coins.png","baboon.jpg","cameraman.png","rice_grains.jpg","barbara.png"]

for i in names:
    srcc=src+i
    img=cv2.imread(srcc,cv2.IMREAD_COLOR)
    hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    ycrcb=cv2.cvtColor(img,cv2.COLOR_BGR2YCrCb)
    R,G,B=cv2.split(img)
    H,S,V=cv2.split(hsv)
    Y,cr,cb=cv2.split(ycrcb)
    
    N=["R","G","B","H","S","V","Y","U","V"]
    M=[R,G,B,H,S,V,Y,cr,cb]

    
    print(i+" "+"RGB"+":",img[20,25])
    print(i+" "+"HSV"+":",hsv[20,25])
    print(i+" "+"YUV"+":",ycrcb[20,25])
    
    cv2.imwrite("Origin"+i,img)
    
    for j in range(0,9):
        cv2.imwrite(N[j]+"_"+i,M[j])




