import numpy as np
import cv2

#create 300 by 300 image. the 3 is for the r g b values. uint8 so it takes 8 bit integers (non-negative), what we'll be using
canvas = np.zeros((300,300,3), dtype = "uint8")

#establish colors
red = (0,0,255)
green = (0,255,0)
blue = (255,0,0)
yellow = (0,255,255)

#draw green line starting at the top left of the canvas spanning across it diagonally to the bottom right
cv2.line(canvas, (0,0), (300,300), green)
cv2.imshow("Luke", canvas)
cv2.waitKey(0)
#draw red line starting at the bottom left of the canvas, spanning across it diagonally to the top right
cv2.line(canvas, (300,0), (0,300), red)
cv2.imshow("Luke vs. Vader", canvas)
cv2.waitKey(0)

#draw blue 60x60 square in the bottom left
cv2.rectangle(canvas,(60,240), (0,300), blue, -1)
cv2.imshow("Vader's Lightsaber Hilt", canvas)
cv2.waitKey(0)

cv2.rectangle(canvas,(240,240), (300,300), blue, -1)
cv2.imshow("Luke's Lightsaber Hilt", canvas)
cv2.waitKey(0)

cv2.rectangle(canvas,(120,120), (180,180), yellow, 5)
cv2.imshow("Clash!", canvas)
cv2.waitKey(0)
