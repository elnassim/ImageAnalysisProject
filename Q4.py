# GI2 2024-2025 - By Sadki Mohamed and El Kaddaoui Nassim, students at the National School of Applied sciences of Tetouan

import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import os

matplotlib.use('Agg') 

img = cv2.imread("Sadki.jpg")

if img is None:
    raise FileNotFoundError("L'image spécifiée n'a pas pu être chargée.")

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

plt.figure(figsize=(10, 5))
plt.hist(img_gray.ravel(), bins=256, color='black', alpha=0.7, label='Niveaux de gris')
plt.title("Histogramme de l'image en niveaux de gris")
plt.xlabel("Intensité de la couleur")
plt.ylabel("Nombre de pixels")
plt.legend()

output_file = "Histogramme_gris.png"
plt.savefig(output_file)

os.startfile(output_file) 
