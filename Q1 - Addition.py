import cv2
import numpy as np
import os
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')

I1 = cv2.imread('Image1.bmp', cv2.IMREAD_GRAYSCALE)
I2 = cv2.imread('Image2.bmp', cv2.IMREAD_GRAYSCALE)
if I1 is None or I2 is None:
    raise FileNotFoundError("Un ou les deux fichiers (I1.bmp, I2.bmp) n'ont pas pu etre chargées" )

L = 256
Ia = np.minimum(I1 + I2, L - 1) 
Ia_img = Ia.astype(np.uint8)
cv2.imwrite("Ia.bmp", Ia_img)
plt.imshow(Ia_img, cmap='gray')
plt.title("Image résultante de l'addition I1 + I2")
plt.axis('off')
output_file = 'Addition.png'

plt.savefig(output_file)
print(f"Resulting image saved as {output_file}")
os.startfile(output_file)


