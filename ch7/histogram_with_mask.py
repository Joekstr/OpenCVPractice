from matplotlib import pyplot as plt
import numpy as np
import argparse
import cv2

def plot_histogram(image, title, mask = None):
    channels = cv2.split(image)
    colors = ('b','g','r')
    plt.figure()
    plt.title(title)
    plt.xlabel("Bins")
    plt.ylabel("Pixels")

    for (channel, color) in zip(channels, colors):
        hist = cv2.calcHist([channel],[0], mask, [256], [0,256])
        plt.plot(hist,color = color)
        plt.xlim([0,256])

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "image path")
args = vars(ap.parse_args())

image = cv2.imread(args['image'])
cv2.imshow('DREAM', image)
plot_histogram(image, "Histogram for DREAM")

mask = np.zeros(image.shape[:2], dtype = "uint8")
cv2.rectangle(mask,(92,95),(315,325),255,-1)
cv2.imshow("THAT'S WHAT THE POINT OF THE MASK IS", mask)

masked = cv2.bitwise_and(image,image,mask = mask)
cv2.imshow("no one cared who i was until i put on the mask", masked)

plot_histogram(image, "Histogram for Masked Image", mask = mask)
plt.show()
cv2.waitKey(0)
