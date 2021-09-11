import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument('-i','--image',required=True,help='image path')
args = vars(ap.parse_args())

image = cv2.imread(args['image'])
image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(image,(5,5),0)
cv2.imshow("BIG GUY STARE", image)

(T, thresh) = cv2.threshold(blurred,155,255,cv2.THRESH_BINARY)
cv2.imshow("Thresh from the Hunger Games",thresh)

(T,threshInv) = cv2.threshold(blurred,155,255,cv2.THRESH_BINARY_INV)
cv2.imshow("Inverse Thresh",threshInv)

cv2.imshow("Phantom of the Opera", cv2.bitwise_and(image,image,mask=threshInv))
cv2.waitKey(0)
