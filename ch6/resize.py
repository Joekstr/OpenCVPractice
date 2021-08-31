import numpy as np
import argparse
import imutils
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i","--image", required = True, help = "image path")
args = vars(ap.parse_args())

image = cv2.imread(args['image'])
cv2.imshow("ENRAGED", image)

r = 150.0/image.shape[1]
dim = (150, int(image.shape[0] * r))


resized = cv2.resize(image,dim,interpolation = cv2.INTER_AREA)
cv2.imshow("short PepeLaugh", resized)

r = 50.0/image.shape[0]
dim = (int(image.shape[1]*r), 50)

resized = cv2.resize(image,dim,interpolation = cv2.INTER_AREA)
cv2.imshow("ittititbitbtitbit", resized)

resized = imutils.resize(image, height = 25)
cv2.imshow("PUNY", resized)
cv2.waitKey(0)
