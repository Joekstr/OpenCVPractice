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

#show image
cv2.imshow("jermaThing", image)
#end process at press of key
cv2.waitKey(0)
cv2.imwrite("jpgandy.jpg", image)
