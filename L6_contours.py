import cv2 as cv
import numpy as np

img = cv.imread('Photos/cat.jpeg')
cv.imshow('Cat', img)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)

# convert to Grayscale

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# blur image

blur = cv.GaussianBlur(gray, (5, 5), cv.BORDER_DEFAULT)
cv.imshow('Blurred', blur)

# # get edges using canny edge detector

canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges', canny)

# thresholding instead of blur and canny edge detector

ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow("Thresh", thresh)
# get the contours

contours, hierarchies = cv.findContours(thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
print(f'{len(contours)} contour(s) found!')

cv.drawContours(blank, contours, -1, (0, 255, 0), 1)
cv.imshow('Contours Drawn', blank)

# contours, hierarchies = cv.findContours(canny, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
# print(f'{len(contours)} contour(s) found!')

# cv.drawContours(blank, contours, -1, (0, 0, 255), 1)
# cv.imshow('Canny Contours', blank)
cv.waitKey(0)