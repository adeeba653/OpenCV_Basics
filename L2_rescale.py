import cv2 as cv

def changeRes(width, height):
    width = capture.set(3, width)
    height = capture.set(4, height)

def rescale(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)  

# img = cv.imread('Photos/lady.jpeg')
# img_resized = rescale(img)

# cv.imshow('Lady resized', img_resized)
# cv.imshow('Lady', img)

# cv.waitKey(0)


capture = cv.VideoCapture(0)
changeRes(100, 100)
while True:
    isTrue, frame = capture.read()
    # frame_resized = rescale(frame, scale=0.2)

    # cv.imshow('live resized', frame_resized)
    cv.imshow('live', frame)
    

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()