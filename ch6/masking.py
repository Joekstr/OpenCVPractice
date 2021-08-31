import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "image path")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Wanted!", image)

size = 75
positionX = -175
positionY = 175
mask = np.zeros(image.shape[:2],dtype = "uint8")
(cX,cY) = ((image.shape[1]//2) + positionX,(image.shape[0]//2) +  positionY)
cv2.rectangle(mask, (cX-size,cY-size),(cX+size,cY+size), 255, -1)
cv2.imshow("Mask by Dream", mask)

masked = cv2.bitwise_and(image,image,mask=mask)
cv2.imshow("GOTEEM", masked)
cv2.waitKey(0)
