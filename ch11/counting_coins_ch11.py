from __future__ import print_function
import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "image path")
args = vars(ap.parse_args())

image = cv2.imread(args['image'])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray,(5,5),0)
cv2.imshow('mogus', image)

edged = cv2.Canny(blurred,30,500)
cv2.imshow('edgy', edged)
(cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
print("I count {} crewmates in this image".format(len(cnts)))

crewmates = image.copy()
cv2.drawContours(crewmates,cnts,-1,(0,255,0),2)
cv2.imshow("SUSSY BAKAS", crewmates)

for (i,c) in enumerate(cnts):
    (x,y,w,h) = cv2.boundingRect(c)

    print("Crewmate #:{}".format(i + 1))
    coin = image[y:y + h, x:x + w]
    cv2.imshow("SUS", coin)

    mask = np.zeros(image.shape[:2], dtype = "uint8")
    ((centerX,centerY),radius) = cv2.minEnclosingCircle(c)
    cv2.circle(mask,(int(centerX),int(centerY)),int(radius),255,-1)
    mask = mask[y:y+h,x:x+w]
    cv2.imshow("SUSSY IMPOSTER",cv2.bitwise_and(coin,coin,mask=mask))
    cv2.waitKey(0)
