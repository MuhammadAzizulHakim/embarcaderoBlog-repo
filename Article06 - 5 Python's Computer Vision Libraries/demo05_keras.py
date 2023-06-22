# Prepare paths of input images and target segmentation masks
import os
 
input_dir = "C:/Users/YOUR_USERNAME/images/"
target_dir = "C:/Users/YOUR_USERNAME/annotations/trimaps/"
img_size = (160, 160)
num_classes = 3
batch_size = 32
 
input_img_paths = sorted(
    [
        os.path.join(input_dir, fname)
        for fname in os.listdir(input_dir)
        if fname.endswith(".jpg")
    ]
)
target_img_paths = sorted(
    [
        os.path.join(target_dir, fname)
        for fname in os.listdir(target_dir)
        if fname.endswith(".png") and not fname.startswith(".")
    ]
)
 
print("Number of samples:", len(input_img_paths))
 
for input_path, target_path in zip(input_img_paths[:10], target_img_paths[:10]):
    print(input_path, "|", target_path)
 
# What does one input image and corresponding segmentation mask look like?
import matplotlib.pyplot as plt
from IPython.display import Image, display
from tensorflow.keras.preprocessing.image import load_img
import PIL
from PIL import ImageOps
import glob
import matplotlib.image as mpimg
 
# Display input image #7
#display(Image(filename=input_img_paths[9]))
gbr = mpimg.imread(input_img_paths[9])
imgplot = plt.imshow(gbr)
plt.show()
 
# Display auto-contrast version of corresponding target (per-pixel categories)
img = PIL.ImageOps.autocontrast(load_img(target_img_paths[9]))
plt.imshow(img)
plt.show()