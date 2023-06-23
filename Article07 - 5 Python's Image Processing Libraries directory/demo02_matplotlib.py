import numpy as np
import matplotlib.pyplot as plt
from matplotlib.image import imread

img = imread('C:/Users/ASUS/stinkbug.png')

# Load image as a NumPy array
print(type(img))
print(img)

# Show image
plt.imshow(img)
plt.show()
