#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2
import numpy as np

source = cv2.imread('/Users/tom/Downloads/drive-download-20171106T182415Z-001/source_img.jpg',0)
temp = cv2.imread('/Users/tom/Downloads/drive-download-20171106T182415Z-001/template_img.jpg',0)

sh = source.shape[0]
sw = source.shape[1]
print("sourceh:",sh)
th = temp.shape[0]
tw = temp.shape[1]
print("temph:",th)
step = 10

avgt = np.mean(temp)
vart = np.var(temp)

ncc = 0
x = 0
y = 0
for i in range (0,sh-th,step):
    for j in range (0,sw-tw,step):
        cr = source[i:(i+th),j:(j+tw)]
        avgcr = np.mean(cr)
        varcr = np.var(cr)
        co = 1/(th*tw*vart*varcr)
        summ = 0
        for m in range(0,th):
            for n in range(0,tw):
                summ += (cr[m][n]-avgcr)*(temp[m][n]-avgt)
                
        if summ*co>ncc:
            ncc = summ*co
            x = j
            y = i
            
result = cv2.cvtColor(source,cv2.COLOR_GRAY2RGB)
            
r=(0,0,255)
cv2.line(result,(x,y),(x,y+th),r,thickness=5)
cv2.line(result,(x,y),(x+tw,y),r,thickness=5)
cv2.line(result,(x+tw,y),(x+tw,y+th),r,thickness=5)
cv2.line(result,(x,y+th),(x+tw,y+th),r,thickness=5)
cv2.imwrite("result.jpg",result)
               
      
       
       
    
