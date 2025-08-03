import cv2 as cv
import numpy as np

blank = np.zeros((500,  500, 3), dtype='uint8')
cv.imshow('Blank', blank)

# 1.Paint image a particular color
blank[200:300, 300:400] = 0, 255, 0 
cv.imshow("Green", blank)
blank[:] = 0, 0, 255 
cv.imshow("Red", blank)
blank[:] = 0, 0, 0 
cv.imshow("Red", blank)

# 2. Draw a rectangle 
cv.rectangle(blank, (0, 0), (250, 250), (255, 0, 0), thickness=cv.FILLED)
cv.imshow('Rectangle', blank)

# 3. draw a circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0, 255, 0), thickness=-1)
cv.imshow('Circle', blank)

# 4. draw a line
cv.line(blank, (0, 0), (blank.shape[1]//2, blank.shape[0]//2), (255, 0, 255), thickness=2)
cv.imshow('line',blank)

# 5. write text
cv.putText(blank, 'Hello', (300 , 300), cv.FONT_HERSHEY_DUPLEX, 2.0, (0, 255, 255), 2,)
cv.imshow('Text', blank)



cv.waitKey(0)