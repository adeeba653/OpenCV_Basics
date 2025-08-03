import cv2 as cv
import numpy as np

img = cv.imread('Photos/Switzerland.jpeg')
cv.imshow('Switzerland', img)

# Translation
def translate(img, x, y):
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

# -x --> left
# -y --> up
# x --> right
# y --> down

translated = translate(img, 100, -200)
cv.imshow('Translated', translated)


# Rotation
def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint=(width//2, height//2)
    
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimension = (width, height)

    return cv.warpAffine(img, rotMat, dimension)

rotated = rotate(img, -45)
rotated_rotated = rotate(rotated, 45)
cv.imshow('Rotated', rotated)
cv.imshow('Rotated Rotated', rotated_rotated)


# Resizing
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

# Flipping
flipped1 = cv.flip(img, 0)
flipped2 = cv.flip(img, 1)
flipped3 = cv.flip(img, -1)

cv.imshow("Flipped", flipped3)

cv.waitKey(0)
