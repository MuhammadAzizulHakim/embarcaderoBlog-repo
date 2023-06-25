import matplotlib.pyplot as plt
import numpy as np
from scipy import ndimage as ndi

import plotly
import plotly.express as px
from skimage import data

# Load image
data = data.kidney()

print(f'number of dimensions: {data.ndim}')
# Dimensions are provided in the following order: (z, y, x, c), i.e., [plane, row, column, channel]:
print(f'shape: {data.shape}')
print(f'dtype: {data.dtype}')

# Dimensions are provided in the following order: (z, y, x, c), i.e., [plane, row, column, channel]:
n_plane, n_row, n_col, n_chan = data.shape

# Display both grayscale and RGB(A) 2D images
_, ax = plt.subplots()
ax.imshow(data[n_plane // 2])
plt.show()

# According to the warning message, the range of values is unexpected. The image rendering is clearly not satisfactory colour-wise.
vmin, vmax = data.min(), data.max()
print(f'range: ({vmin}, {vmax})')

# Turn to plotly’s implementation of the imshow function, for it supports value ranges beyond (0.0, 1.0) for floats and (0, 255) for integers.
fig = px.imshow(data[n_plane // 2], zmax=vmax)
#plotly.io.show(fig)
fig.show()
