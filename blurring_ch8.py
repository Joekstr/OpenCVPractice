import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required = True, help = 'image path')
args = vars(ap.parse_args())

image = cv2.imread(args['image'])
cv2.imshow('SMASH BROS SANDY', image)

#average blur
blurred = np.hstack([
    cv2.blur(image,(9,9)),
    cv2.blur(image,(15,15)),
    cv2.blur(image,(21,21))])
cv2.imshow("AVERAGE ANDY",blurred)

#gaussian blur
blurred = np.hstack([
    cv2.GaussianBlur(image,(9,9),0),
    cv2.GaussianBlur(image,(15,15),0),
    cv2.GaussianBlur(image,(21,21),0)])
cv2.imshow("GAUSSIAN GARY",blurred)

#median blur
blurred = np.hstack([
    cv2.medianBlur(image,9),
    cv2.medianBlur(image,15),
    cv2.medianBlur(image,21)])
cv2.imshow("MEDIAN MARY", blurred)

#bilateral blur
blurred = np.hstack([
    cv2.bilateralFilter(image,9,62,62),
    cv2.bilateralFilter(image,15,93,93),
    cv2.bilateralFilter(image,21,123,123)])
cv2.imshow("BILATERAL BARRY", blurred)
cv2.waitKey(0)
