import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread('./amban.jpg', cv2.IMREAD_GRAYSCALE)
kernel_size = 6
min_filtered_img = cv2.erode(img, np.ones((kernel_size, kernel_size), np.uint8), iterations=1)
max_filtered_img = cv2.dilate(img, np.ones((kernel_size, kernel_size), np.uint8), iterations=1)
plt.subplot(1, 3, 1)
plt.imshow(img, cmap='gray')
plt.title('Ảnh Gốc')
plt.axis('off')
plt.subplot(1, 3, 2)
plt.imshow(min_filtered_img, cmap='gray')
plt.title('Toán tử láng giềng min')
plt.axis('off')
plt.subplot(1, 3, 3)
plt.imshow(max_filtered_img, cmap='gray')
plt.title('láng giềng max')
plt.axis('off')
plt.show()