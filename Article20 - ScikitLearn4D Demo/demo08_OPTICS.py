# Optics clustering
from numpy import unique
from numpy import where
from sklearn.datasets import make_classification
from sklearn.cluster import OPTICS
import matplotlib.pyplot as plt
matplotlib.use("Agg")

# Define dataset
X, _ = make_classification(n_samples=1000, n_features=2, n_informative=2, n_redundant=0, n_clusters_per_class=1, random_state=4)
# Define the model
model = OPTICS(eps=0.8, min_samples=10)
# Fit model and predict clusters
yhat = model.fit_predict(X)
# Retrieve unique clusters
clusters = unique(yhat)

# Create scatter plot for samples from each cluster
for cluster in clusters:
    # get row indexes for samples with this cluster
    row_ix = where(yhat == cluster)
    # create scatter of these samples
    plt.scatter(X[row_ix, 0], X[row_ix, 1])
# Show the plot
plt.savefig("scikitlearnImage.jpg")
