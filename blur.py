#importing modules
import cv2 
from matplotlib import pyplot as plt

#loading photos fro disk
photo=cv2.imread("p1.jpeg")
photo=cv2.cvtColor(photo,cv2.COLOR_BGR2RGB)
plt.imshow(photo)

#initializing kernel
k=(15,15)

#Normal Blur
blur_img=cv2.blur(photo,k)
blur_img=cv2.cvtColor(blur_img,cv2.COLOR_RGB2BGR)
plt.imshow(blur_img)
cv2.imwrite("blur.jpg",blur_img)

#GaussianBlur
gb = cv2.GaussianBlur(photo,(15,15),0)
gb=cv2.cvtColor(gb,cv2.COLOR_RGB2BGR)
plt.imshow(gb)
cv2.imwrite("gb.jpg",gb)

#Median Blurring
median = cv2.medianBlur(photo,15)
median=cv2.cvtColor(median,cv2.COLOR_RGB2BGR)
plt.imshow(median)
cv2.imwrite("m-blur.jpg",median)

#BilateralFilter Blurring
photo=cv2.imread('e.jpg')
photo=cv2.cvtColor(photo,cv2.COLOR_BGR2RGB)
b_blur = cv2.bilateralFilter(photo,9,575,575)
b_blur=cv2.cvtColor(b_blur,cv2.COLOR_RGB2BGR)
plt.imshow(b_blur)
cv2.imwrite("b-blur.jpg",b_blur)
