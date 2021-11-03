from typing import Counter
import cv2
import numpy as np
import matplotlib.pyplot as plt 

img = np.zeros((200,360), dtype = 'uint8')
img [:,:] = 255



for i in range(200):
    for j in range (360):
        if i == 79 and 170<= j <= 190:
            img[i][j] = 0


for i in range(200):
    for j in range (360):
        if 180 < i + j < 200:
            img[i, j] = 0


for i in range (200):
    for j  in range(180,360):
        img [i][j:j+20] =0

img [70:85, 110:250] = 0
       

cv2.imshow('output',img)
cv2.waitKey()