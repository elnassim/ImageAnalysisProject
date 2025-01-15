import cv2
import numpy as np
import os
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg') 

img = cv2.imread("Sadki.jpg")
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
r, g, b = cv2.split(img_rgb)

plt.figure(figsize=(10, 5))
plt.hist(r.ravel(), bins=256, color='red', alpha=0.5, label='Rouge')
plt.hist(g.ravel(), bins=256, color='green', alpha=0.5, label='Vert')
plt.hist(b.ravel(), bins=256, color='blue', alpha=0.5, label='Bleu')
plt.title("Histogramme du portrait")
plt.xlabel("Intensité de la couleur")
plt.ylabel("Nombre de pixels")
plt.legend()
output_file = 'Histogramme_portrait.png'

plt.savefig(output_file)
print("Resulting image saved as {output_file}")
os.startfile(output_file)
