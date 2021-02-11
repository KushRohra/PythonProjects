import cv2
import random

img = cv2.imread('assets/cat.png', -1)

print(img.shape)  # Height * Width * Channel

# Standard => RBG
# OpenCV => BGR

# Changing part of image to random colors
'''for i in range(100):
    for j in range(img.shape[1]): # Width
        img[i][j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
'''

# Copying part of image and paste that on another part of array
tag = img[250:400, 200:450]
img[0:150, 0:250] = tag

cv2.imshow('Cat', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
