import cv2
import numpy as np
import matplotlib.pyplot as plt
 
image = cv2.imread("C:/Users/YOUR_USERNAME/got.jpg")
 
pts1 = np.float32([[535,145],[625,145],[535,250],[625,250]])
pts2 = np.float32([[0,0],[400,0],[0,400],[400,400]])
 
M = cv2.getPerspectiveTransform(pts1,pts2)
 
dst = cv2.warpPerspective(image,M,(400,400))
 
plt.subplot(121),plt.imshow(image),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()