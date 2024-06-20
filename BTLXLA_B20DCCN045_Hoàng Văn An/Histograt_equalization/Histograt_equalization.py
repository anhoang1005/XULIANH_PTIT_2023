import cv2
import numpy as np
import matplotlib.pyplot as plt
# Đọc ảnh từ đường dẫn
img = cv2.imread('./amban.jpg', cv2.IMREAD_GRAYSCALE)
# Áp dụng histogram equalization
equalized_img = cv2.equalizeHist(img)
# Hiển thị ảnh gốc và ảnh sau khi áp dụng histogram equalization
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(img, cmap='gray')
plt.title('Ảnh Gốc')
plt.axis('off')
plt.subplot(1, 2, 2)
plt.imshow(equalized_img, cmap='gray')
plt.title('Histogram Equalization')
plt.axis('off')
plt.show()