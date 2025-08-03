import cv2 as cv

def rescale(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


capture = cv.VideoCapture(0)

while True:
    isTrue, frame = capture.read()

    frame= rescale(frame, scale=1.2)
    # frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # frame = cv.Canny(frame, 125, 175)
    cv.imshow('Dog', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()


# img = cv.imread('Photos/horse.jpeg')
# img = rescale(img)
# cv.imshow('GROUP', img)

# # BGR to GRAYSCALE
# gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("GRAY",gray_img)

# # BLUR

# blur1 = cv.GaussianBlur(img, (3, 3), cv.BORDER_DEFAULT)
# cv.imshow('BLUR1', blur1)
# blur2 = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)
# cv.imshow('BLUR2', blur2)


# # EDGE CASCADE

# canny = cv.Canny(img, 125, 175)
# cv.imshow('CANNY1', canny)
# canny = cv.Canny(blur1, 125, 175)
# cv.imshow('CANNY2', canny)
# canny = cv.Canny(blur2, 125, 175)
# cv.imshow('CANNY3', canny)

# # dilate
# dilated = cv.dilate(canny, (7,7), iterations=3)
# # erode
# eroded = cv.dilate(dilated, (7,7), iterations=3)

# #resize
# resized = cv.resize(img, (500, 500)) 

# # crop
# cropped = img[20:200, 200:400]
# cv.imshow('Cropped', cropped)
# cv.waitKey(0)