import cv2
import numpy as np
import matplotlib.pyplot as plt 

img = np.zeros((255,255), dtype = 'uint8')
height, width = img.shape

for i in range (height):
    for j in range (width):
        img[i][j] = 255 - i



cv2.imshow('Output', img)
cv2.waitKey()
