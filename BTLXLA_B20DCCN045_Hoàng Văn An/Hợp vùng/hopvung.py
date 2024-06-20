import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread('./amban.jpg', cv2.IMREAD_GRAYSCALE)
region_size = 5
height, width = img.shape[:2]
segments = img.copy()
for y in range(0, height, region_size):
    for x in range(0, width, region_size):
        roi = img[y:y+region_size, x:x+region_size]
        mean_intensity = np.mean(roi)
        segments[y:y+region_size, x:x+region_size] = mean_intensity
plt.subplot(1, 2, 1)
plt.imshow(img, cmap='gray')
plt.title('Ảnh Gốc')
plt.axis('off')
plt.subplot(1, 2, 2)
plt.imshow(segments, cmap='gray')
plt.title('Hợp Vùng')
plt.axis('off')
plt.show()