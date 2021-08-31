import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "image path")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("the most interesting man in the world", image)

y1 = 380
y2 = 530
x1 = 270
x2 = 365

cropped = image[y1:y2,x1:x2]
cv2.imshow("jermaSchnoz",cropped)

cv2.waitKey(0)
