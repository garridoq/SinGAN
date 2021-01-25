import cv2
import numpy as np
model = "picasso_1"
images = ["picasso1","picasso1_f","picasso2","starry_night2"]
scales = [3,4,5,6,7,8]

print("SinGAN PSNRs")
for i in range(len(images)):
    image = images[i]
    ref = cv2.imread("./Input/Denoising/"+image+".png")
    print("================================================")
    for scale in scales:
        path = "./Output/Denoising/"+model+"/"+image+"_noisy_out/start_scale="+str(scale)+".png"
        denoised = cv2.imread(path)
        PSNR = cv2.PSNR(ref,denoised)
        print("PSNR for ", image, "at scale ", scale, " is : ", PSNR)

print()
print("FFDNet PSNRs")

for i in range(len(images)):
    image = images[i]
    print("================================================")
    ref = cv2.imread("./Input/Denoising/"+image+".png")
    denoised = cv2.imread("./classical_denoising/ffdnet/"+image+".png")
    PSNR = cv2.PSNR(ref,denoised)
    print("PSNR for ", image, " is : ", PSNR )

print()
print("BM3D PSNRs")

for i in range(len(images)):
    image = images[i]
    print("================================================")
    ref = cv2.imread("./Input/Denoising/"+image+".png")
    denoised = cv2.imread("./classical_denoising/bm3d/"+image+".png")
    PSNR = cv2.PSNR(ref,denoised)
    print("PSNR for ", image, " is : ", PSNR )
