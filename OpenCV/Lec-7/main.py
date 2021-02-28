import numpy as np
import cv2

# both the images should be resized in such a case
img = cv2.resize(cv2.imread('assests/soccer_practice.jpg', 0), (0, 0), fx=0.5, fy=0.5)
template = cv2.resize(cv2.imread('assests/ball.png', 0), (0, 0), fx=0.5, fy=0.5)  # can do it with the shoe image also

h, w = template.shape

# use all the methods and determine which works best
methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
           cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

for method in methods:
    img2 = img.copy()

    # Base image, template image, method
    result = cv2.matchTemplate(img, template, method)  # does the Convolution to match the template with the image
    # (W - w + 1, H - h + 1)
    # W and H for base image
    # w and h for template image

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        location = min_loc
    else:
        location = max_loc

    bottom_right = (location[0] + w, location[1] + h)
    cv2.rectangle(img2, location, bottom_right, 255, 5)

    cv2.imshow('Match', img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
