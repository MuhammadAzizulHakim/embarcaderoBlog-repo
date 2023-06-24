import os

import numpy as np
import matplotlib.pyplot as plt

import nitime
import nitime.timeseries as ts
import nitime.analysis as nta
import nitime.viz as viz

TR = 2.
len_et = 15  # This is given in number of samples, not time!

# Load Dataset
data_path = os.path.join(nitime.__path__[0], 'data')
fname = os.path.join(data_path, 'event_related_fmri.csv')
data = np.genfromtxt(fname, dtype=float, delimiter=',', names=True)

# One Time Series
t1 = ts.TimeSeries(data['bold'], sampling_interval=TR)
# Another Time Series
t2 = ts.TimeSeries(data['events'], sampling_interval=TR)

# Event-Related Analyzer
E = nta.EventRelatedAnalyzer(t1, t2, len_et)

# Pass the eta and ets calculations straight into the visualization function, and plots the result:
fig01 = viz.plot_tseries(E.eta, ylabel='BOLD (% signal change)', yerror=E.ets)
plt.show()