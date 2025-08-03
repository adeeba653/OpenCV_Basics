import cv2 as cv

img = cv.imread('Photos/group2.jpg')
cv.imshow('People', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray Poeple", gray)

# Face Detection
# 1> reading the haar cascade xml file
haar_cascade = cv.CascadeClassifier('L15_faceDetection/face_haarCascade.xml')

# 2> detecting faces using the haar_cascade
faces_rect = haar_cascade.detectMultiScale(gray, 1.1,3)
print(f'Number of Faces found = {len(faces_rect)}')

# 3> drawing the detcted rectangles on the orginal image
for(x, y, w, h) in faces_rect:
    cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv.imshow('Detected Faces', img)

cv.waitKey(0)