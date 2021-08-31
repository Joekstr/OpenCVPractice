import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "image path")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
(B,G,R) = cv2.split(image)

cv2.imshow("BRIGHT GREY", R)
cv2.imshow("BLACK AND WHITE ANDY", G)
cv2.imshow("jermaMoon", B)

merged = cv2.merge([B,G,R])
cv2.imshow("COLORFUL ANDY", merged)


zeros = np.zeros(image.shape[:2],dtype="uint8")
cv2.imshow("MALDING", cv2.merge([zeros,zeros,R]))
cv2.imshow("MR. GREENZ", cv2.merge([zeros,G,zeros]))
cv2.imshow("jermaPluto", cv2.merge([B,zeros,zeros]))

cv2.waitKey(0)
cv2.destroyAllWindows()
