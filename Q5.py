# GI2 2024-2025 - By Sadki Mohamed and El Kaddaoui Nassim, students at the National School of Applied sciences of Tetouan

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import matplotlib
matplotlib.use('Agg')  

def read_image(filepath, resize_factor):
  
    image = Image.open(filepath).convert('L') 
    if resize_factor < 1.0:
        new_size = (int(image.width * resize_factor), int(image.height * resize_factor))
        image = image.resize(new_size, Image.Resampling.LANCZOS) 
    return np.array(image)

def simple_nagao_filter(image):
   
    height, width = image.shape
    output = np.zeros_like(image)  
    padded = np.pad(image, 2, mode='reflect')  

    for i in range(height):
        for j in range(width):
            window = padded[i:i+5, j:j+5]
            regions = [
                window[0:3, 0:3],  # Haut-gauche
                window[0:3, 2:5],  # Haut-droite
                window[2:5, 0:3],  # Bas-gauche
                window[2:5, 2:5],  # Bas-droite
                window[1:4, 1:4]   # Centre
            ]
            min_var = float('inf')
            best_mean = 0
            for region in regions:
                var = np.var(region)
                if var < min_var:
                    min_var = var
                    best_mean = np.mean(region)
            
            output[i, j] = best_mean

    return output

if __name__ == "__main__":
    try:
        print("Chargement de l'image...")
        image = read_image('Nassim_gris.png', resize_factor=0.5)
        
        print("Application du filtre simplifié...")
        filtered = simple_nagao_filter(image)
        
        plt.figure(figsize=(10, 5))
        
        plt.subplot(1, 2, 1)
        plt.imshow(image, cmap='gray')
        plt.title('Image Originale')
        plt.axis('off')
        plt.subplot(1, 2, 2)
        plt.imshow(filtered, cmap='gray')
        plt.title('Après Filtre Simplifié')
        plt.axis('off')
        plt.tight_layout()
        plt.show()
        plt.imsave('Image_filtre_simplifie.png', filtered, cmap='gray')
        print("Traitement terminé avec succès!")
    except Exception as e:
        print(f"Une erreur est survenue : {e}")



