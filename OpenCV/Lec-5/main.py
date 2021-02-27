import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    width = int(cap.get(3))
    height = int(cap.get(4))

    # HSV => Hue, Saturation, Lightness/Brightness

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_blue = np.array([90, 50, 50])
    upper_blue = np.array([130, 255, 255])

    mask = cv2.inRange(hsv, lower_blue, upper_blue) # Any pixel not in this range will be blacked out
    result = cv2.bitwise_and(frame, frame, mask=mask)
    # 2 src images => takes 2 images and blends them using the mask

    cv2.imshow('frame', result)
    #cv2.imshow('mask', mask)
    # the areas that show up in the mask as white are the ones that remain in the result after bitwise and

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


'''
    BGR_color = np.array([[[255, 0, 0]]])
    x = cv2.cvtColor(BGR_color, cv2.COLOR_BGR2HSV) # expects a image not a single color
    x[0][0] => Access that color
'''