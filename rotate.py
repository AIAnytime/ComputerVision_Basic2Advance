import cv2

img = cv2.imread("data/parrot.jpeg", 1)

#resizing the image by half its current value
img = cv2.resize(img, (0,0), fx=0.5, fy=0.5)

#rotate the image by clockwise,counterclockwise, etc
img = cv2.rotate(img, cv2.cv2.ROTATE_180)

#show the image
cv2.imshow("Image", img)

#write/save the image
cv2.imwrite("new_image.jpg", img)

#close and destroy
cv2.waitKey(0)
cv2.destroyAllWindows()
