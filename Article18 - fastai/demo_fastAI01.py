from fastai.vision.all import *

# Download and decompress dataset
path = untar_data(URLs.PETS)

# Check what is inside with the .ls() method
print(path.ls())

# Grab all the image files (recursively) in one folder and print out the total image files
files = get_image_files(path/"images")
print(len(files))

files[0],files[6]

def label_func(f): return f[0].isupper()
dls = ImageDataLoaders.from_name_func(path, files, label_func, item_tfms=Resize(224))

# Show the image output of this batch
dls.show_batch()
import matplotlib.pyplot as plt
#plt.show()

# Combines the data and a model for training, and uses transfer learning to fine tune a pretrained model
learn = cnn_learner(dls, resnet34, metrics=error_rate)
learn.fine_tune(1)
print(learn.predict(files[0]))

learn.show_results()
plt.show()