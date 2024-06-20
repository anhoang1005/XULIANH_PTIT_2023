import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread('amban.jpg', cv2.IMREAD_GRAYSCALE)
kernel_size = 5
median_filtered_img = cv2.medianBlur(img, kernel_size)
plt.subplot(1, 2, 1)
plt.imshow(img, cmap='gray')
plt.title('Ảnh Gốc')
plt.axis('off')
plt.subplot(1, 2, 2)
plt.imshow(median_filtered_img, cmap='gray')
plt.title('Bộ Lọc Trung Vị')
plt.axis('off')
plt.show()