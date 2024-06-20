import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread('./amban.jpg', cv2.IMREAD_GRAYSCALE)
c = 255 / np.log(1 + np.max(img))
log_transformed_img = c * (np.log(img + 1))
c2 = 255 / np.log(1 + np.max(img))
inverse_log_transformed_img = (2 ** (img / c)) - 1
plt.subplot(1, 3, 1)
plt.imshow(img, cmap='gray')
plt.title('Ảnh Gốc')
plt.axis('off')
plt.subplot(1, 3, 2)
plt.imshow(log_transformed_img, cmap='gray')
plt.title('Logarithmic')
plt.axis('off')
plt.subplot(1, 3, 3)
plt.imshow(inverse_log_transformed_img, cmap='gray')
plt.title('Nghịch Đảo Logarithmic')
plt.axis('off')
plt.show()