import cv2 as cv #Load the library

#load the image and assign it to a variable
#img = cv.imread("data/parrot.jpeg", 0)
#load as BGR
#img = cv.imread("data/parrot.jpeg", -1)
#load as it is
img = cv.imread("data/parrot.jpeg", 1)

"""0= Grayscale Image mode
   -1= BGR Image mode
  1= Same as it containing alpha channel if it is """

#display the image
cv.imshow("Image", img)

"""imshow(Window Name, variable name)"""

#Close the window 
cv.waitKey(0) #wait infinite time until user press any key to close the window
cv.destroyAllWindows()