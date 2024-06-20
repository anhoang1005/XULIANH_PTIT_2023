import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread('./amban.jpg', cv2.IMREAD_GRAYSCALE)
kernel_size = 5
mean_filtered_img = cv2.blur(img, (kernel_size, kernel_size))
plt.subplot(1, 2, 1)
plt.imshow(img, cmap='gray')
plt.title('Ảnh Gốc')
plt.axis('off')
plt.subplot(1, 2, 2)
plt.imshow(mean_filtered_img, cmap='gray')
plt.title('Bộ Lọc Trung Bình')
plt.axis('off')
plt.show()