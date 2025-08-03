import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np


img = cv.imread('Photos/coffee.jpeg')
cv.imshow('Coffee', img)

blank = np.zeros((img.shape[:2]), dtype='uint8')

#  creating a mask
circle = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2-100), 100, 255, -1)

# Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('GRAY', gray)

# Masked Grayscale
masked = cv.bitwise_and(gray, gray, mask=circle)
cv.imshow('Masked Image', masked)

# GRAYSCALE Histogram
gray_hist = cv.calcHist([gray], [0], None, [256], [0,256])
plt.figure()
plt.title('Grayscale histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
plt.plot(gray_hist)
plt.xlim([0, 256])
plt.show()


#  COLOR Histogram
# plt.figure()
# plt.title('Grayscale histogram')
# plt.xlabel('Bins')
# plt.ylabel('# of pixels')
# colors = ('b', 'g', 'r')
# for i,col in enumerate(colors):
#     color_hist = cv.calcHist([img], [i], circle, [256], [0, 256])
#     plt.plot(color_hist, color=col)
#     plt.xlim([0, 256])


# plt.show()








cv.waitKey(0)
