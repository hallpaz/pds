import numpy as np
import matplotlib.pyplot as plt
import cv2

# Função para calcular a DCT 2D
def dct2(image):
    return cv2.dct(np.float32(image))

# Função para calcular a IDCT 2D
def idct2(dct_coeffs):
    return cv2.idct(dct_coeffs)

# Carregar uma imagem em escala de cinza
image = cv2.imread('example_image.jpg', cv2.IMREAD_GRAYSCALE)
if image is None:
    raise FileNotFoundError("Certifique-se de que a imagem 'example_image.jpg' está no diretório atual.")

# Calcular a DCT
image_dct = dct2(image)

# Zero os coeficientes de alta frequência para compressão
threshold = 0.1 * np.max(image_dct)
compressed_dct = np.where(np.abs(image_dct) > threshold, image_dct, 0)

# Reconstruir a imagem a partir da DCT comprimida
reconstructed_image = idct2(compressed_dct)

# Visualizar resultados
plt.figure(figsize=(12, 8))

plt.subplot(1, 3, 1)
plt.title("Imagem Original")
plt.imshow(image, cmap='gray')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.title("Coeficientes da DCT")
plt.imshow(np.log1p(np.abs(image_dct)), cmap='gray')  # Log para melhor visualização
plt.axis('off')

plt.subplot(1, 3, 3)
plt.title("Imagem Reconstruída")
plt.imshow(reconstructed_image, cmap='gray')
plt.axis('off')

plt.tight_layout()
plt.show()
