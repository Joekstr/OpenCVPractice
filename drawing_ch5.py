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
cv2.line(canvas, (0,0), (300,300), green, 10)
cv2.imshow("Luke", canvas)
cv2.waitKey(0)
#draw red line starting at the bottom left of the canvas, spanning across it diagonally to the top right
cv2.line(canvas, (300,0), (0,300), red, 10)
cv2.imshow("Luke vs. Vader", canvas)
cv2.waitKey(0)

#draw blue 60x60 solid square in the bottom left
cv2.rectangle(canvas,(60,240), (0,300), (100,100,100), -1)
cv2.imshow("Vader's Lightsaber Hilt", canvas)
cv2.waitKey(0)

#draw blue 60x60 solid square in the bottom right
cv2.rectangle(canvas,(240,240), (300,300), (100,100,100), -1)
cv2.imshow("Luke's Lightsaber Hilt", canvas)
cv2.waitKey(0)

#draw yellow non-filled box in the middle of the screen
cv2.rectangle(canvas,(120,120), (180,180), yellow, 5)
cv2.imshow("Clash!", canvas)
cv2.waitKey(0)

#new canvas for circles
canvas = np.zeros((300,300,3),dtype="uint8")
#get center of canvas
(centerX, centerY) = (canvas.shape[1]//2, canvas.shape[0]//2)
#establish white
white = (255,255,255)

#range from 0 to 175, step 25
for r in range(0,175,5):
    #create circles with increasing radii
    cv2.circle(canvas, (centerX,centerY),r,np.random.randint(0,high=256, size =(3,)).tolist(), 5)

#show circles
cv2.imshow("Bullseye", canvas)
cv2.waitKey(0)

for i in range(0,500):
    #establish random parameters for circle
    radius = np.random.randint(5, high=50)
    color = np.random.randint(0,high=256, size =(3,)).tolist()
    pt = np.random.randint(0,high=300,size = (2,))
    cv2.circle(canvas,tuple(pt),radius, color, -1)

#show circle
cv2.imshow("Ball Pit",canvas)
cv2.waitKey(0)
