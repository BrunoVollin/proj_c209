import cv2
import numpy as np


def nothing(x):
    pass


cap = cv2.VideoCapture(0)

cv2.namedWindow('Web Cam')
cv2.namedWindow('Set HSV')

cv2.createTrackbar('HMin', 'Set HSV', 0, 179, nothing)
cv2.createTrackbar('HMax', 'Set HSV', 0, 179, nothing)
cv2.createTrackbar('SMin', 'Set HSV', 0, 255, nothing)
cv2.createTrackbar('SMax', 'Set HSV', 0, 255, nothing)
cv2.createTrackbar('VMin', 'Set HSV', 0, 255, nothing)
cv2.createTrackbar('VMax', 'Set HSV', 0, 255, nothing)


cv2.setTrackbarPos('HMax', 'Set HSV', 179)
cv2.setTrackbarPos('SMax', 'Set HSV', 255)
cv2.setTrackbarPos('VMax', 'Set HSV', 255)


hMin = 0
sMin = 0
vMin = 0
hMax = 0
sMax = 0
vMax = 0

while(1):
    _, image = cap.read()

    hMin = cv2.getTrackbarPos('HMin', 'Set HSV')
    sMin = cv2.getTrackbarPos('SMin', 'Set HSV')
    vMin = cv2.getTrackbarPos('VMin', 'Set HSV')
    hMax = cv2.getTrackbarPos('HMax', 'Set HSV')
    sMax = cv2.getTrackbarPos('SMax', 'Set HSV')
    vMax = cv2.getTrackbarPos('VMax', 'Set HSV')

    lower = np.array([hMin, sMin, vMin])
    upper = np.array([hMax, sMax, vMax])

    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower, upper)
    result = cv2.bitwise_and(image, image, mask=mask)

    imf = cv2.resize(result, (960, 540))
    mask = cv2.resize(mask, (960, 540))

    background_image = cv2.imread('C:/images/bg.png')
    print(background_image)
    background_image = cv2.cvtColor(background_image, cv2.COLOR_BGR2RGB)

    crop_background = background_image[0:960, 0:960]

    crop_background[mask != 0] = [0, 0, 0]

    final_image = imf + crop_background  

    cv2.imshow('Web Cam', final_image)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
