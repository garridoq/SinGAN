import sys
import numpy as np
import random
import cv2

def gaussian_noise(image,mu=0,sigma=30):
    noise = np.random.normal(mu, sigma, image.shape) 
    image = image + noise
    return image

image = cv2.imread(sys.argv[1])
noise_img = gaussian_noise(image)
cv2.imwrite(sys.argv[1][:-4] + '_noisy.png', noise_img)
