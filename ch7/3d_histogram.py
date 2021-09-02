from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "image path")
ap.add_argument("-s", "--size", required = False, help = "size of largest bin",default = 5000)
ap.add_argument("-b", "--bins", required = False, help = "number of bins per color", default = 8)
args = vars(ap.parse_args())

image = cv2.imread(args['image'])
cv2.imshow('le epic amphibia', image)
cv2.waitKey(0)
size = float(args['size'])
bins = int(args['bins'])

hist = cv2.calcHist([image], [0,1,2], None, [bins,bins,bins], [0,256,0,256,0,256])

print("3D histo shape: %s, with %d values"%(hist.shape, hist.flatten().shape[0]))

fig = plt.figure()
ax = fig.add_subplot(111,projection="3d")
ratio = size/np.max(hist)

for(x,plane) in enumerate(hist):
    for(y,row) in enumerate(plane):
        for(z,col) in enumerate(row):
            if hist[x][y][z] > 0.0:
                siz = ratio * hist[x][y][z]
                rgb = (z/(bins-1),y/(bins-1),x/(bins-1))
                ax.scatter(x,y,z,s=siz,facecolor=rgb)

plt.show()
