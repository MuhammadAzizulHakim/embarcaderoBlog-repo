import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# Generate synthetic stock market data
np.random.seed(42)
X = np.linspace(0, 10, 100).reshape(-1, 1)
y = np.sin(X).ravel() + np.random.normal(scale=0.1, size=X.shape[0])

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize the data
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

class RBFNetwork:
    def __init__(self, num_input, num_hidden, num_output, sigma=1.0):
        self.num_input = num_input
        self.num_hidden = num_hidden
        self.num_output = num_output
        self.sigma = sigma
        self.centers = None
        self.weights = None

    def _calculate_centers(self, X):
        idx = np.random.choice(X.shape[0], self.num_hidden, replace=False)
        centers = X[idx]
        return centers

    def _compute_activation(self, X):
        activation = np.zeros((X.shape[0], self.num_hidden))
        for i in range(self.num_hidden):
            activation[:, i] = np.exp(-np.linalg.norm(X - self.centers[i], axis=1) ** 2 / (2 * self.sigma ** 2))
        return activation

    def fit(self, X, y):
        self.centers = self._calculate_centers(X)
        activation = self._compute_activation(X)
        self.weights = np.dot(np.linalg.pinv(activation), y)

    def predict(self, X):
        activation = self._compute_activation(X)
        output = np.dot(activation, self.weights)
        return output

# Initialize RBF network
num_hidden_neurons = 10
rbf_net = RBFNetwork(num_input=X_train_scaled.shape[1], num_hidden=num_hidden_neurons, num_output=1, sigma=1.0)

# Train the network
rbf_net.fit(X_train_scaled, y_train)

# Make predictions
y_train_pred = rbf_net.predict(X_train_scaled)
y_test_pred = rbf_net.predict(X_test_scaled)

# Evaluate the model
train_mse = mean_squared_error(y_train, y_train_pred)
test_mse = mean_squared_error(y_test, y_test_pred)

print(f'Train MSE: {train_mse:.4f}')
print(f'Test MSE: {test_mse:.4f}')

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(X, y, 'b-', label='True Data')
plt.plot(X_train, y_train_pred, 'ro', label='Train Predictions')
plt.plot(X_test, y_test_pred, 'go', label='Test Predictions')
plt.legend()
plt.xlabel('X')
plt.ylabel('y')
plt.title('RBF Network - Stock Market Prediction')
plt.show()
