import numpy as np
import argparse
import imutils
import cv2

#get and show image
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "image path")
args = vars(ap.parse_args())
image = cv2.imread(args["image"])
cv2.imshow("NORMAL ANDY", image)

#establish the translation matrix
M = np.float32([[1,0,100], [0,1,200]])
#apply the translation
shifted = cv2.warpAffine(image,M,(image.shape[1],image.shape[0]))
cv2.imshow("BOTTOM RIGHT ANDY", shifted)

#establish the translation matrix
M = np.float32([[1,0,-200],[0,1,-360]])
#apply the translation
shifted = cv2.warpAffine(image,M,(image.shape[1],image.shape[0]))
cv2.imshow("UPPER LEFT ANDY", shifted)

shifted = imutils.translate(image,0,400)
cv2.imshow("Shifted Down",shifted)
cv2.waitKey(0)
