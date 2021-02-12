import cv2

#load an image in grayscale
img = cv2.imread("data/parrot.jpeg", 0)
#resize the image and pass height*width value
#img = cv2.resize(img, (400,400))

#if want to shrink the image by half or double the image, we can use fx and fy
#img = cv2.resize(img, (0,0), fx=0.5, fy=0.5) #shrink the image by half
img = cv2.resize(img, (0,0), fx=2, fy=2) #shrink the image by double

#display the image
cv2.imshow("Image", img)

#close window
cv2.waitKey(0)
cv2.destroyAllWindows()