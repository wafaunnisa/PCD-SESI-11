import imageio as img
import numpy as np
import matplotlib.pyplot as plt 

def isOne(m):
    a = m[0][0]
    b = m[0][1]
    c = m[1][0]
    d = m[1][1]
    return (a * d) - (b * c) == 1

def decrypt(image, m):
    if not isOne(m):
        return "Determinan Matriks harus 1"
    result = np.zeros_like(image)
    d = m[0][0]
    b = 256-m[0][1]
    c = 256-m[1][0]
    a = m[1][1]
    for i in range(0, image.shape[0] - 1, 2):
        for j in range(0, image.shape[1]):
            r1 = ((image[i, j, 0] * a) + (image[i + 1, j, 0] * c)) % 256
            r2 = ((image[i, j, 0] * b) + (image[i + 1, j, 0] * d)) % 256

            g1 = ((image[i, j, 1] * a) + (image[i + 1, j, 1] * c)) % 256
            g2 = ((image[i, j, 1] * b) + (image[i + 1, j, 1] * d)) % 256

            b1 = ((image[i, j, 2] * a) + (image[i + 1, j, 2] * c)) % 256
            b2 = ((image[i, j, 2] * b) + (image[i + 1, j, 2] * d)) % 256

            result[i, j, 0] = r1
            result[i + 1, j, 0] = r2
            result[i, j, 1] = g1
            result[i + 1, j, 1] = g2
            result[i, j, 2] = b1
            result[i + 1, j, 2] = b2
    return result

image = img.imread("enc.png")
m = np.array([
    [3, 2],
    [7, 5],
])
imgDec = decrypt(image, m)

plt.figure(figsize=(10, 10))
plt.subplot(1, 3, 1)
plt.imshow(image)
plt.subplot(1, 3, 2)
plt.imshow(imgDec)
plt.show()

