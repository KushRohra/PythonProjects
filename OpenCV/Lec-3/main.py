import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    width = int(cap.get(3))  # 3 is the number of width
    height = int(cap.get(4))  # 4 is the number of height

    # Shape => rows, columns, channels : exact shape as frame
    image = np.zeros(frame.shape, np.uint8)
    smaller_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)

    image[:height // 2, :width // 2] = cv2.rotate(smaller_frame, cv2.cv2.ROTATE_180)  # Top Left
    image[height // 2:, :width // 2] = smaller_frame  # Bottom Left
    image[:height // 2, width // 2:] = cv2.rotate(smaller_frame, cv2.cv2.ROTATE_180)  # Top Right
    image[height // 2:, width // 2:] = smaller_frame  # Bottom Right

    cv2.imshow('frame', image)

    if cv2.waitKey(1) == ord('q'):
        break

# Release the resource
cap.release()
cv2.destroyAllWindows()
