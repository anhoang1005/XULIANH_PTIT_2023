import cv2
import numpy as np
import matplotlib.pyplot as plt
def split_region(img, min_region_size):
    height, width = img.shape[:2]
    regions = [(0, 0, width, height)]
    while regions:
        region = regions.pop()
        x, y, w, h = region
        roi = img[y:y+h, x:x+w]
        std_dev = np.std(roi)
        if std_dev > min_region_size:
            regions.extend([(x, y, w//2, h//2),
                (x + w//2, y, w//2, h//2),
                (x, y + h//2, w//2, h//2),
                (x + w//2, y + h//2, w//2, h//2)])

        else:
            img[y:y+h, x:x+w] = np.mean(roi)
    return img
img = cv2.imread('./amban.jpg', cv2.IMREAD_GRAYSCALE)
min_region_size = 10
result_img = split_region(img.copy(), min_region_size)
plt.subplot(1, 2, 1)
plt.imshow(img, cmap='gray')
plt.title('Ảnh Gốc')
plt.axis('off')
plt.subplot(1, 2, 2)
plt.imshow(result_img, cmap='gray')
plt.title('Tách Vùng')
plt.axis('off')
plt.show()