import cv2 as cv
import numpy as np

img = cv.imread('Photos/horse.jpeg')
cv.imshow('horse', img)

blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('Blank', blank)

# splitting into three img each displaying only one of the three color channels of original img
b, g, r= cv.split(img)

cv.imshow("Blue", b)
cv.imshow("Green", g)
cv.imshow("Red", r)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)


# merging the components b, g, r to get original img
merged = cv.merge([b, g, r])
cv.imshow("Merged", merged)

# render the blue component as blue on blank
blue = cv.merge([b, blank, blank])
cv.imshow('BLUEasblue', blue)

# render the green component as green on blank
green = cv.merge([blank, g, blank])
cv.imshow('GREENasgreen', green)

# render the red component as red on blank
red = cv.merge([blank, blank, r])
cv.imshow('REDasred', red)


print(blue.shape)
print(green.shape)
print(red.shape)


cv.waitKey(0)