import cv2 as cv
import numpy as np

img = cv.imread("Photos/horse.jpeg")
cv.imshow('Horse', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Laplacian Edge Detection
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian Edges', lap)

# Sobel Edege Detection
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
sobel = cv.bitwise_or(sobelx, sobely)

cv.imshow('Sobel X', sobelx)
cv.imshow('Sobel Y', sobely)
cv.imshow('Sobel Edges', sobel)

# Canny - more advanced and multi-stage edegedetection , uses sobel in one of its stages
canny = cv.Canny(gray, 125,  175)
cv.imshow("Canny edges", canny)


cv.waitKey(0)