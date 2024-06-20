import cv2
import numpy as np
import matplotlib.pyplot as plt

# Đọc ảnh
img = cv2.imread('amban.jpg')

# Kiểm tra xem ảnh đã đọc được hay chưa
if img is not None:
    # Chuyển đổi sang ảnh âm bản
    negative_img = 255 - img

    # Hiển thị ảnh gốc và ảnh âm bản
    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.title('Ảnh Gốc')
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.imshow(cv2.cvtColor(negative_img.astype(np.uint8), cv2.COLOR_BGR2RGB))
    plt.title('Ảnh Âm Bản')
    plt.axis('off')

    plt.show()
else:
    print("Không thể đọc ảnh. Đường dẫn hoặc file ảnh không tồn tại.")
