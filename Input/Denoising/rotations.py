import cv2
import sys
import numpy as np
import matplotlib.pyplot as plt
import imutils

image = sys.argv[1]
im = cv2.imread(image)
for rot in range(-20,21,5):
    print(rot)
    rotated = imutils.rotate(im,angle=rot)
    noise = np.random.normal(0, 30, rotated.shape) 
    rotated = rotated + noise
    cv2.imwrite("rotations/"+image.split(".")[0]+"_noisy_"+str(rot)+".png",rotated)
for rot in range(-4,6,1):
    print(rot)
    rotated = imutils.rotate(im,angle=rot)
    noise = np.random.normal(0, 30, rotated.shape) 
    rotated = rotated + noise
    cv2.imwrite("rotations/"+image.split(".")[0]+"_noisy_"+str(rot)+".png",rotated)
