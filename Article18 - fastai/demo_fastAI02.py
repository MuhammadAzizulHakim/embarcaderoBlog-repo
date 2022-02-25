from fastai.vision.all import *
from nbdev.showdoc import *

set_seed(42)

# Batch size
bs = 64

# Look at the data
## Untar data
help(untar_data)
## Path to the data
path = untar_data(URLs.PETS); path
## Display all paths relative to dataset root
Path.BASE_PATH = path
path.ls()
## Take a look at the data and its annotations
path_anno = path/'annotations'
path_img = path/'images'
## Gets the labels from the filenames using a regular expression
fnames = get_image_files(path_img)
fnames

dls = ImageDataLoaders.from_name_re(path, fnames, pat=r'(.+)_\d+.jpg$', item_tfms=Resize(460), bs=bs, batch_tfms=[*aug_transforms(size=224, min_scale=0.75), Normalize.from_stats(*imagenet_stats)])
## Show image
dls.show_batch(max_n=9, figsize=(7,6))
import matplotlib.pyplot as plt
plt.show()
## Print image annotation vocabularies
print(dls.vocab)
len(dls.vocab),dls.c

# Training: resnet34
## We will train for 4 epochs (4 cycles through all our data).
learn = cnn_learner(dls, resnet34, metrics=error_rate).to_fp16()
## The implemented models
learn.model
## Learning
learn.fit_one_cycle(4)
## Save the learning stage
learn.save('stage-1')

# Results
interp = ClassificationInterpretation.from_learner(learn)
losses,idxs = interp.top_losses()
len(dls.valid_ds)==len(losses)==len(idxs)
## Plotting results
interp.plot_top_losses(9, figsize=(15,11))
plt.show()
## Plotting confusion matrix
interp.plot_confusion_matrix(figsize=(12,12), dpi=60)
plt.show()

interp.most_confused(min_val=2)