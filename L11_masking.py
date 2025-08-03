import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('Photos/lady.jpeg')
cv.imshow('Lady', img)

# plt.imshow(img)
# plt.show()

blank = np.zeros(img.shape[:2], dtype='uint8')
# cv.imshow('Blank Image', blank)

# mask = cv.circle(blank, (img.shape[1]//2+130, img.shape[0]//2-170), 150, 255, -1)
# cv.imshow('Mask', mask)

# masked = cv.bitwise_and(img, img, mask=mask)
# cv.imshow('Masked Image', masked)

circle = cv.circle(blank.copy(), (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
rectangle = cv.rectangle(blank.copy(), (200, 200), (500, 400), 255, -1)
cv.imshow("Circle", circle)
weird_shape= cv.bitwise_and(circle, rectangle)
cv.imshow('Weird Shape', weird_shape)

masked = cv.bitwise_and(img, img, mask=weird_shape)
cv.imshow("Weird Shape Masked Image", masked)
cv.waitKey(0)