import cv2

# Read an image
img = cv2.imread('assests/cat.png', 1)

# Resize an image
img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)  # Resize to half size
# img = cv2.resize(img, (400, 400))      #Resisze to a fixed size

# Rotate the image
img = cv2.rotate(img, cv2.cv2.ROTATE_90_CLOCKWISE)

# Save the new image
cv2.imwrite('assests/newCat.png', img)


'''
    cv2.IMREAD_COLOR(-1) => Loads a color image. Any transparency will be neglected. defult mode
    cv2.IMREAD_GRAYSCALE(0) => Loads a image in grayscale mode
    cv2.IMREAD_UNCHANGED(1) => Loads a image as such including alpha channel
'''

# Show the image
cv2.imshow('Cat', img)
cv2.waitKey(0)  # 0 => wait an infinte amount of time until a key is pressed
cv2.destroyAllWindows()
