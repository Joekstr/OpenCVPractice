from __future__ import print_function
from matplotlib import pyplot as plt
import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "/Users/josephaguilar/Documents/GitHub/OpenCVPractice/ch7/amphibia.jpeg")
args = vars(ap.parse_args())

image = cv2.imread(args['image'])
cv2.imshow("THE phibia", image)

channels = cv2.split(image)
colors = ('b','g','r')
plt.figure()
plt.title("Color Histogram")
plt.xlabel("Bins")
plt.ylabel("Pixels")

for (channel, color) in zip(channels, colors):
    hist = cv2.calcHist([channel],[0],None,[256],[0,250])
    plt.plot(hist,color=color)
    plt.xlim([0,256])

fig = plt.figure()

ax = fig.add_subplot(131)
hist = cv2.calcHist([channels[1], channels[0]], [0,1], None, [32,32], [0,256,0,256])
p = ax.imshow(hist,interpolation="nearest")
ax.set_title("G and B")
plt.colorbar(p)

ax = fig.add_subplot(132)
hist = cv2.calcHist([channels[1], channels[2]], [0,1], None, [32,32], [0,256,0,256])
p = ax.imshow(hist,interpolation="nearest")
ax.set_title("G and R")
plt.colorbar(p)

ax = fig.add_subplot(133)
hist = cv2.calcHist([channels[0], channels[2]], [0,1], None, [32,32], [0,256,0,256])
p = ax.imshow(hist,interpolation="nearest")
ax.set_title("R and B")
plt.colorbar(p)

print("2D Histogram Shape: {}, with {} values".format(hist.shape, hist.flatten().shape[0]))

hist = cv2.calcHist([image], [0,1,2], None, [8,8,8], [0,256,0,256,0,256])
print("3D Histogram Shape: {}, with {} values".format(hist.shape,hist.flatten().shape[0]))
plt.show()
cv2.waitKey(0)
