import cv2
import matplotlib.pyplot as plt
img = cv2.imread('amban.jpg', cv2.IMREAD_GRAYSCALE)
canny_img = cv2.Canny(img, 50, 150)
plt.subplot(1, 2, 1)
plt.imshow(img, cmap='gray')
plt.title('Ảnh Gốc')
plt.axis('off')
plt.subplot(1, 2, 2)
plt.imshow(canny_img, cmap='gray')
plt.title('Canny')
plt.axis('off')
plt.show()