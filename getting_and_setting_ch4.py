from __future__ import print_function
import argparse
import cv2
#set up arguments to store image into a variable and execute the code
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
    help = "image path")
args = vars(ap.parse_args())
#store image in a variable
image = cv2.imread(args["image"])

#take pixel(s) and get r,g,b valuess
x1 = 60
y1 = 180
x2 = 160
y2 = 280
(b,g,r) = image[x1,y1]
print("Pixel at ({}, {}) - Red : {}, Green: {}, Blue: {}".format(x1,y1,r,g,b))
#change rgb value of pixel
image[x1,y1] = (0,0,255)
(b,g,r) = image [x1,y1]
print("Pixel at ({}, {}) - Red : {}, Green: {}, Blue: {}".format(x1,y1,r,g,b))
#get and show corner
corner = image[x1:x2, y1:y2]
cv2.imshow("CORNER CREEP", corner)

#show image
cv2.imshow("jermaThing", image)

#turn corner green
image[x1:x2, y1:y2] = (128,0,128)
cv2.imshow("EYEPATCH ANDY", image)

#end process at press of key
cv2.waitKey(0)
