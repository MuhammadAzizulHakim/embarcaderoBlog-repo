import numpy as np
import matplotlib.pyplot as plt
from sklearn.kernel_approximation import RBFSampler
from sklearn.linear_model import Ridge

# Generate a sample signal (e.g., a noisy sine wave)
np.random.seed(42)
n_samples = 100
X = np.linspace(0, 4 * np.pi, n_samples).reshape(-1, 1)
y = np.sin(X).ravel() + np.random.normal(scale=0.1, size=n_samples)

# Plot the original noisy signal
plt.figure(figsize=(10, 6))
plt.plot(X, y, label='Noisy signal')
plt.title('Original Noisy Signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.legend()
plt.show()

# Use RBFSampler to approximate the RBF kernel
rbf_sampler = RBFSampler(gamma=1.0, n_components=100, random_state=42)
X_features = rbf_sampler.fit_transform(X)

# Train a Ridge regression model on the RBF features
model = Ridge(alpha=1.0)
model.fit(X_features, y)

# Predict the signal using the trained model
y_pred = model.predict(X_features)

# Plot the original noisy signal and the filtered signal
plt.figure(figsize=(10, 6))
plt.plot(X, y, label='Noisy signal')
plt.plot(X, y_pred, label='Filtered signal', color='red')
plt.title('Signal Processing using RBFN')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.legend()
plt.show()
