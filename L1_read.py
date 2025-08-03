import cv2 as cv

# reading an image

img = cv.imread('Photos/cat.jpeg')
cv.imshow('Cat', img)
cv.waitKey(0)


# reading a video
capture = cv.VideoCapture(0)

while True:
    isTrue, frame = capture.read()
    cv.imshow('Dog', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()