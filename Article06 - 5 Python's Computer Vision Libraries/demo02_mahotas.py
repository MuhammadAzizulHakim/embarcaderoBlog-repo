import mahotas as mh
import numpy as np
from pylab import imshow, gray, show, subplot
from os import path

# Load your own photo
originalPhoto = mh.demos.load('cat')
# Load photo in grayscale
photo = mh.demos.load('cat', as_grey=True)

# Convert to integer values (using numpy operations)
photo = photo.astype(np.uint8)

# Compute Riddler-Calvard threshold
T_rc = mh.rc(photo)
thresholded_rc = (photo > T_rc)

# Now call pylab functions to display the image
subplot(2,1,1)
imshow(originalPhoto)
subplot(2,1,2)
imshow(thresholded_rc)
show()