import cv2 as cv

img = cv.imread('Photos/dog.jpeg')
cv.imshow('Dog', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Simple Thresholding
threshold, thresh = cv.threshold(gray, 140, 255, cv.THRESH_BINARY)
cv.imshow('Simple Thresholded', thresh)
# Inverse Simple Thresholding
threshold, thresh_inv = cv.threshold(gray, 140, 255, cv.THRESH_BINARY_INV)
cv.imshow('Simple Thresholded Inv', thresh_inv)

# Adaptive Thresholding
adaptive_thresh_mean = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3)
cv.imshow('Adaptive Thresholded Mean', adaptive_thresh_mean)

adaptive_thresh_gauss = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 15, 1)
cv.imshow('Adaptive Thresholded Gaussian', adaptive_thresh_gauss)

cv.waitKey(0)