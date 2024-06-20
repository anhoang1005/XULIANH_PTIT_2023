import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread('./amban.jpg', cv2.IMREAD_GRAYSCALE)
# Áp dụng thuật toán Otsu
_, otsu_threshold_img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
plt.subplot(1, 2, 1)
plt.imshow(img, cmap='gray')
plt.title('Ảnh Gốc')
plt.axis('off')
plt.subplot(1, 2, 2)
plt.imshow(otsu_threshold_img, cmap='gray')
plt.title('Thuật Toán Otsu')
plt.axis('off')
plt.show()