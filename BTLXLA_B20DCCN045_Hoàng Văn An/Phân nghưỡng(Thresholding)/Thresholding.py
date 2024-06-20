import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread('amban.jpg', cv2.IMREAD_GRAYSCALE)
_, thresholded_img = cv2.threshold(img, 1, 255, cv2.THRESH_BINARY)
plt.subplot(1, 2, 1)
plt.imshow(img, cmap='gray')
plt.title('Ảnh Gốc')
plt.axis('off')
plt.subplot(1, 2, 2)
plt.imshow(thresholded_img, cmap='gray')
plt.title('Ảnh Sau Phân Ngưỡng')
plt.axis('off')
plt.show()