# GI2 2024-2025 - By Sadki Mohamed and El Kaddaoui Nassim, students at the National School of Applied sciences of Tetouan

import cv2
import numpy as np
import os
import matplotlib.pyplot as plt
import matplotlib

matplotlib.use('Agg')

I1 = cv2.imread('Image1.bmp', cv2.IMREAD_GRAYSCALE)
I2 = cv2.imread('Image2.bmp', cv2.IMREAD_GRAYSCALE)

if I1 is None or I2 is None:
    raise FileNotFoundError("One or both image files ('I1.bmp', 'I2.bmp') could not be loaded. Please check the file paths.")

S = np.maximum(I1 - I2, 0) 

S_img = S.astype(np.uint8)

cv2.imwrite("Is.bmp", S_img)

plt.imshow(S_img, cmap='gray')
plt.title("Image résultante de la soustraction I1 - I2")
plt.axis('off')
output_file = 'Soustraction.png'
plt.savefig(output_file)
print(f"Resulting image saved as {output_file}")

os.startfile(output_file)  

