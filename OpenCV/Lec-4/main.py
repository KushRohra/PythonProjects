import numpy as num
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    width = int(cap.get(3))
    height = int(cap.get(4))

    img = cv2.line(frame, (0,0), (width, height), (255, 0, 0), 10)  # coordinate for starting and ending position of the line
    # Image, starting pos, ending pos, color(bgr), thickness

    img = cv2.line(img, (0, height), (width, 0), (0, 255, 0), 5)


    # Rectangle => top left, bottom right
    img = cv2.rectangle(img, (100, 100), (200, 200), (128, 128, 128), 5)
    # If in the place of thickness you put -1 you get a filled rectangle

    # Circle => Image, Center pos, radius, color, thickness
    img = cv2.circle(img, (300, 300), 60, (0, 0, 255), -1)


    # Text => Bottom left hand color
    font = cv2.FONT_HERSHEY_SIMPLEX
    img = cv2.putText(img, 'Kush Rohra', (10, height - 10), font, 2, (0, 0, 0), 5, cv2.LINE_AA)
    # Image, text, bottom left pos, font style, fontScale(fontSize),color, thickness, lineType(optional)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()