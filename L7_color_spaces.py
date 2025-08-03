import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('Photos/dog.jpeg')
cv.imshow('Dog', img)


# BGR to GRAY
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('GRAY', gray)

# BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow("HSV", hsv)

# BGR to L*A*B
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow("LAB", lab)

# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow("RGB", rgb)

# matplotlib displays image in rgb
# plt.imshow(rgb)
# plt.show()

# GRAY --> BGR
gray_bgr = cv.cvtColor(gray, cv.COLOR_GRAY2BGR)
cv.imshow("GRAY-->BGR", gray_bgr)

red = gray_bgr.copy()
green = gray_bgr.copy()
blue = gray_bgr.copy()

red[:, :, 0] = 0 # remove blue
red[:, :, 1] = 0 # remove green


blue[:, :, 1] = 0 # remove green
blue[:, :, 2] = 0 # remove red

green[:, :, 0] = 0 # remove blue
green[:, :, 2] = 0 # remove red

cv.imshow("BLUE", blue)
cv.imshow("GREEN", green)
cv.imshow("RED", red)


# HSV --> BGR
# hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
# cv.imshow("HSV-->BGR", hsv_bgr)

# LAB --> BGR
# lab_bgr = cv.cvtColor(lab, cv.COLOR_LAB2BGR)
# cv.imshow("LAB-->BGR", lab_bgr)

# RGB --> BGR
# rgb_bgr = cv.cvtColor(rgb, cv.COLOR_RGB2BGR)
# cv.imshow("RGB-->BGR", rgb_bgr)

# GRAY --> LAB/HSV
# gray_hsv = cv.cvtColor(gray_bgr, cv.COLOR_BGR2HSV)
# cv.imshow("GRAY-->HSV", gray_hsv)
# gray_lab = cv.cvtColor(gray_bgr, cv.COLOR_BGR2LAB)
# cv.imshow("GRAY-->LAB", gray_lab)



cv.waitKey(0)
