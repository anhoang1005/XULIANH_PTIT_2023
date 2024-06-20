import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread('amban.jpg', cv2.IMREAD_GRAYSCALE)
n = 0.3
power_law_transformed_img = np.power(img / 255.0, n) * 255.0
plt.subplot(1, 2, 1)
plt.imshow(img, cmap='gray')
plt.title('Ảnh Gốc')
plt.axis('off')
plt.subplot(1, 2, 2)
plt.imshow(power_law_transformed_img, cmap='gray')
plt.title(f'Biến Đổi Hàm Mũ (n={n})')
plt.axis('off')
plt.show()