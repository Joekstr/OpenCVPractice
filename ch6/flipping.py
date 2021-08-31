import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "image path")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("i LOVE raddishes!!!", image)

flip = cv2.flip(image,1)
cv2.imshow("!!!sehsiddar EVOL i", flip)

flip = cv2.flip(image,0)
cv2.imshow("UPSIDE DOWN ANDY", flip)

flip = cv2.flip(image, -1)
cv2.imshow("YDNA NWOD EDISPU", flip)

cv2.waitKey(0)
