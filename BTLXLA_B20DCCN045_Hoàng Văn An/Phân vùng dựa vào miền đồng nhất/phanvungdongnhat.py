import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread('./amban.jpg', cv2.IMREAD_GRAYSCALE)
seed_point = (100, 100)
mask = np.zeros((img.shape[0] + 2, img.shape[1] + 2), np.uint8)
region_growing_img = img.copy()
cv2.floodFill(region_growing_img, mask, seed_point, 255)
plt.subplot(1, 2, 1)
plt.imshow(img, cmap='gray')
plt.title('Ảnh Gốc')
plt.axis('off')
plt.subplot(1, 2, 2)
plt.imshow(region_growing_img, cmap='gray')
plt.title('Phát Triển Vùng')
plt.axis('off')
plt.show()