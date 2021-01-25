import cv2
import numpy as np
import matplotlib.pyplot as plt
import imutils

model = "dublin_1"
image = "dublin1"
#rots =[-20,-15,-10,-5,-4,-3,-2,-1,0,1,2,3,4,5,10,15,20]
rots = [0,1,2,5,10,15]
scales = [3,4,5,6,7,8]

print("SinGAN PSNRs")
ref = cv2.imread("./Input/Denoising/"+image+".jpg")
mask = np.ones_like(ref)
for rot in rots:
    print(f"Rot : {rot} ================================================")
    mask_rot = imutils.rotate(mask,angle=rot)
    ref_rot = imutils.rotate(ref,angle=rot)*mask_rot
    for scale in scales:
        path = "./Output/Denoising/"+model+"/rotations/"+image+"_noisy_"+str(rot)+"_out/start_scale="+str(scale)+".png"
        denoised = cv2.imread(path)*mask_rot
        PSNR = cv2.PSNR(ref_rot,denoised)
        print("PSNR for ", image, "at scale ", scale, " is : ", PSNR)

print("FFDnet PSNRs")
for rot in rots:
    print(f"Rot : {rot} ================================================")
    mask_rot = imutils.rotate(mask,angle=rot)
    ref_rot = imutils.rotate(ref,angle=rot)*mask_rot
    path = "./classical_denoising/rotations/"+image+"_noisy_"+str(rot)+"_f.png"
    denoised = cv2.imread(path)*mask_rot
    PSNR = cv2.PSNR(ref_rot,denoised)
    print("PSNR for ", image, " is : ", PSNR)



print("BM3d PSNRs")
for rot in rots:
    print(f"Rot : {rot} ================================================")
    mask_rot = imutils.rotate(mask,angle=rot)
    ref_rot = imutils.rotate(ref,angle=rot)*mask_rot
    path = "./classical_denoising/rotations/"+image+"_noisy_"+str(rot)+"_b.png"
    denoised = cv2.imread(path)*mask_rot
    PSNR = cv2.PSNR(ref_rot,denoised)
    print("PSNR for ", image, " is : ", PSNR)
