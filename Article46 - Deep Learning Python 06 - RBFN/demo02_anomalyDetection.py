import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_classification
from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score
import scipy.spatial.distance as distance

class RadialBasisFunctionNeuralNetwork:
    def __init__(self, num_of_rbf_units=10):
        self.num_of_rbf_units = num_of_rbf_units

    def _rbf_unit(self, rbf_center, point_in_dataset):
        return np.exp(-self.beta * distance.cdist([point_in_dataset], [rbf_center], 'euclidean')**2).flatten()[0]

    def _construct_interpolation_matrix(self, input_dataset):
        interpolation_matrix = np.zeros((len(input_dataset), self.num_of_rbf_units))
        for idx, point_in_dataset in enumerate(input_dataset):
            for center_idx, rbf_center in enumerate(self.rbf_centers):
                interpolation_matrix[idx, center_idx] = self._rbf_unit(rbf_center, point_in_dataset)
        return interpolation_matrix

    def train_model(self, input_dataset, target_dataset):
        self.kmeans_clustering = KMeans(n_clusters=self.num_of_rbf_units, random_state=0).fit(input_dataset)
        self.rbf_centers = self.kmeans_clustering.cluster_centers_
        self.beta = 1.0 / (2.0 * (self.kmeans_clustering.inertia_ / input_dataset.shape[0]))
        interpolation_matrix = self._construct_interpolation_matrix(input_dataset)
        self.model_weights = np.linalg.pinv(interpolation_matrix.T.dot(interpolation_matrix)).dot(interpolation_matrix.T).dot(target_dataset)

    def predict(self, input_dataset):
        interpolation_matrix = self._construct_interpolation_matrix(input_dataset)
        predicted_values = interpolation_matrix.dot(self.model_weights)
        return predicted_values


if __name__ == "__main__":
    # Generating a simple classification dataset
    input_dataset, target_dataset = make_classification(n_samples=500, n_features=2, n_informative=2, n_redundant=0, n_classes=2)

    # Initializing and training the RBF neural network
    rbf_neural_network = RadialBasisFunctionNeuralNetwork(num_of_rbf_units=20)
    rbf_neural_network.train_model(input_dataset, target_dataset)

    # Predicting the target values
    predictions = rbf_neural_network.predict(input_dataset)

    # Converting continuous output to binary labels
    binary_predictions = np.where(predictions > 0.5, 1, 0)

    # print("Accuracy: {}".format(accuracy_score(target_dataset, binary_predictions)))
    print(f"Accuracy: {accuracy_score(target_dataset, binary_predictions)}")

    # Plotting the results
    plt.scatter(input_dataset[:, 0], input_dataset[:, 1], c=binary_predictions, cmap='viridis', alpha=0.7)
    plt.scatter(rbf_neural_network.rbf_centers[:, 0], rbf_neural_network.rbf_centers[:, 1], c='red')
    plt.title('Classification Result')
    plt.show()