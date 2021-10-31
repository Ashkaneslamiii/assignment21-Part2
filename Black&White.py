import cv2

img = cv2.imread('m.png',0)
img = cv2.resize(img, (255,255))
height, width = img.shape

for i in range (height):
    for j in range (width):
        img[i][j] = 255 - i



cv2.imshow('Output', img)
cv2.waitKey()
