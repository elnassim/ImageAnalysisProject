# GI2 2024-2025 - By Sadki Mohamed and El Kaddaoui Nassim, students at the National School of Applied sciences of Tetouan

import cv2
import numpy as np
import os
import matplotlib.pyplot as plt
import matplotlib

matplotlib.use('Agg')
image_I = np.array([
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 3, 3, 4, 4, 5, 5, 6, 0],
    [0, 3, 3, 4, 4, 5, 5, 6, 0],
    [0, 6, 6, 5, 5, 4, 4, 3, 0],
    [0, 7, 8, 9, 7, 8, 9, 7, 0],
    [0, 9, 9, 8, 8, 7, 7, 7, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
], dtype=np.uint8)

ratio = 2

max_value = 15

image_M = np.minimum(image_I * ratio, max_value)

image_M_bmp = (image_M / max_value * 255).astype(np.uint8)

cv2.imwrite("Im.bmp", image_M_bmp)
plt.imshow(image_M_bmp, cmap='gray', vmin=0, vmax=255)
plt.title(f"Image résultante (Multiplication par {ratio} sur 4 bits)")
plt.axis('off')
output_file = 'Multiplication.png'
plt.savefig(output_file)
print(f"Resulting image saved as {output_file}")

os.startfile(output_file) 

