# GI2 2024-2025 - By Sadki Mohamed and El Kaddaoui Nassim, students at the National School of Applied sciences of Tetouan

import cv2
import numpy as np
import os
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg') 

def afficher_et_sauvegarder_image(image, titre, nom_fichier):
    plt.imshow(image, cmap='gray')
    plt.title(titre)
    plt.axis('off')
    plt.savefig(nom_fichier)
    plt.close()
    os.startfile(nom_fichier)

choix = input("Choisissez le type d'image à générer (1 pour binaire, 2 pour niveau de gris) : ")

image_path = 'Sadki.jpg'
image = cv2.imread(image_path)

if image is None:
    raise FileNotFoundError("L'image spécifiée n'a pas pu être chargée.")
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
if choix == '1':
    image_binaire = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, image_binaire = cv2.threshold(image_binaire, 127, 255, cv2.THRESH_BINARY)
    afficher_et_sauvegarder_image(image_binaire, "Image Binaire", 'Image_binaire.png')
elif choix == '2':
    nb_bits = int(input("Entrez le nombre de bits pour l'image en niveau de gris (par exemple 8, 4, 1) : "))
    image_gris = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    max_value = 2**nb_bits - 1
    image_gris_quantifiee = np.floor(image_gris / (256 / (max_value + 1))) * (256 / (max_value + 1))
    image_gris_quantifiee = np.uint8(image_gris_quantifiee)
    afficher_et_sauvegarder_image(image_gris_quantifiee, f"Image en {nb_bits} bits", 'Image_gris_quantifiee.png')
else:
    print("Choix invalide.")



