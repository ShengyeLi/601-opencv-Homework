#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2
import numpy as np

def Add_gaussian_Noise(pic, mean, sigma):
    
    noice_pic=pic.copy()
    cv2.randn(noice_pic,mean,sigma)
    cv2.add(pic, noice_pic, noice_pic)
    
    return noice_pic

def Add_salt_pepper_Noise(pic, pa, pb):
    amount1 = int(pic.shape[0]*pic.shape[1]*pa)
    amount2 = int(pic.shape[0]*pic.shape[1]*pb)
    
    noisepic=pic
    
    for i in range(amount1):
        noisepic[np.random.randint(0,pic.shape[0]-1), np.random.randint(0,pic.shape[1]-1)]=0
        
    for i in range(amount2):
        noisepic[np.random.randint(0,pic.shape[0]-1), np.random.randint(0,pic.shape[1]-1)]=255
        
    return noisepic

def main():
    mean = 0
    sigma = 100
    pa = 0.01
    pb = 0.01
    src="/Users/tom/Downloads/OpenCV_homework/Test_images/" 
    pic = cv2.imread(src+"Lenna.png")
    
    gray = cv2.cvtColor(pic,cv2.COLOR_BGR2GRAY)
    cv2.imwrite("LennaGray.png",gray)
    
    gauss_noiseImage = Add_gaussian_Noise(gray,mean,sigma)
    cv2.imwrite("gaussiannoise.png",gauss_noiseImage)
    pepper_saltImage=Add_salt_pepper_Noise(gray,pa,pb)
    cv2.imwrite("peppersaltnoise.png",pepper_saltImage)
    
    x=[0,5,10,20]
    y=[0.01,0.03,0.05,0.4]
    for i in x:
        for j in x:
            gnoise=Add_gaussian_Noise(pic, i, j)
            temp = np.square(pic - gnoise).mean()
            m=str(i)
            n=str(j)
            print("mean:"+m+" "+",sigma:"+n+" noise value:",temp)
        
    for i in y:
        for j in y:
            pnoise=Add_salt_pepper_Noise(pic, i, j)
            temp = np.square(pic - pnoise).mean()
            m=str(i)
            n=str(j)
            print("pa:"+m+" "+",pb:"+n+" noise value:",temp)

    for i in range (1,4):
        k=2*i+1
        s=str(k)
        
        boxfilter_img = cv2.boxFilter(gauss_noiseImage, -1, (k, k))
        cv2.imwrite(s+"*"+s+"_"+"gaussianBoxfilter1.png",boxfilter_img)
        gaussfilter_img=cv2.GaussianBlur(gauss_noiseImage, (k,k), 1.5, 3)
        cv2.imwrite(s+"*"+s+"_"+"gaussianGaussfilter2.png",gaussfilter_img)
        medianfilter_img=cv2.medianBlur(gauss_noiseImage,5)
        cv2.imwrite(s+"*"+s+"_"+"gaussianMedianfilter3.png",medianfilter_img)
        
        boxfilter_img = cv2.boxFilter(pepper_saltImage, -1, (k, k))
        cv2.imwrite(s+"*"+s+"_"+"peppersaltBoxfilter1.png",boxfilter_img)
        gaussfilter_img=cv2.GaussianBlur(pepper_saltImage, (k,k), 1.5, 3)
        cv2.imwrite(s+"*"+s+"_"+"peppersaltGaussfilter2.png",gaussfilter_img)
        medianfilter_img=cv2.medianBlur(pepper_saltImage,5)
        cv2.imwrite(s+"*"+s+"_"+"peppersaltMedianfilter3.png",medianfilter_img)
    
if __name__ == "__main__":
    main()
