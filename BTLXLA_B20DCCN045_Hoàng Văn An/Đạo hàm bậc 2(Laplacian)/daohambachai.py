import cv2
import matplotlib.pyplot as plt
img = cv2.imread('amban.jpg', cv2.IMREAD_GRAYSCALE)
laplacian_img = cv2.Laplacian(img, cv2.CV_64F)
plt.subplot(1, 2, 1)
plt.imshow(img, cmap='gray')
plt.title('Ảnh Gốc')
plt.axis('off')
plt.subplot(1, 2, 2)
plt.imshow(laplacian_img, cmap='gray')
plt.title('Laplacian')
plt.axis('off')
plt.show()