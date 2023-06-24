import pandas as pd
import numpy as np
import matplotlib.pylab as plt
from pydse.arma import ARMA

# Create a Simple ARMA Model for a 2-D Output Vector with Matrices:
AR = (np.array([1, .5, .3, 0, .2, .1, 0, .2, .05, 1, .5, .3]), np.array([3, 2, 2]))
MA = (np.array([1, .2, 0, .1, 0, 0, 1, .3]), np.array([2, 2, 2]))
arma = ARMA(A=AR, B=MA, rand_state=0)

# Create Simulation:
sim_data = arma.simulate(sampleT=100)
sim_index = pd.date_range('1/1/2011', periods=sim_data.shape[0], freq='d')
df = pd.DataFrame(data=sim_data, index=sim_index)
df.plot()

# Check the Autocorrelation Function and Partial Autocorrelation Function:
from statsmodels.graphics.tsaplots import plot_pacf, plot_acf

sim_data = arma.simulate(sampleT=3000)
sim_index = pd.date_range('1/1/2011', periods=sim_data.shape[0], freq='d')
df = pd.DataFrame(data=sim_data, index=sim_index)
plot_acf(df[0], lags=10)
plot_pacf(df[0], lags=10)
plt.show()