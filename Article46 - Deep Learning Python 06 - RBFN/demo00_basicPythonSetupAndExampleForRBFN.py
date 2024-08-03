import numpy as np
from scipy.spatial.distance import cdist
from sklearn.cluster import KMeans
from sklearn.linear_model import LinearRegression

class RBFN:
    def __init__(self, num_centers, spread):
        self.num_centers = num_centers
        self.spread = spread
    def _rbf(self, X, centers, spread):
        return np.exp(-cdist(X, centers) ** 2 / (2 * spread ** 2))
    def fit(self, X, y):
        # Step 1: Use k-means to find centers
        kmeans = KMeans(n_clusters=self.num_centers)
        kmeans.fit(X)
        self.centers = kmeans.cluster_centers_
        # Step 2: Calculate the RBF activations
        RBF_X = self._rbf(X, self.centers, self.spread)
        # Step 3: Train linear regression on RBF activations
        self.regressor = LinearRegression()
        self.regressor.fit(RBF_X, y)
    def predict(self, X):
        RBF_X = self._rbf(X, self.centers, self.spread)
        return self.regressor.predict(RBF_X)

# Sample usage
if __name__ == "__main__":
    from sklearn.datasets import make_regression
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import mean_squared_error
    # Generate synthetic data
    X, y = make_regression(n_samples=100, n_features=2, noise=0.1)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    # Initialize and train RBFN
    rbfn = RBFN(num_centers=10, spread=1.0)
    rbfn.fit(X_train, y_train)
    # Predict and evaluate
    y_pred = rbfn.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    print(f"Mean Squared Error: {mse}")
    # Plot results
    import matplotlib.pyplot as plt
    plt.scatter(y_test, y_pred)
    plt.xlabel("True Values")
    plt.ylabel("Predictions")
    plt.title("RBFN Predictions vs True Values")
    plt.show()
