from tslearn.utils import to_time_series_dataset

my_first_time_series = [1, 3, 4, 2]
my_second_time_series = [1, 2, 4, 2]
my_third_time_series = [1, 2, 4, 2, 2]
X = to_time_series_dataset([my_first_time_series,
                            my_second_time_series,
                            my_third_time_series])
y = [0, 1, 1]

# Time Series Data Preprocessing
from tslearn.preprocessing import TimeSeriesScalerMinMax
X_scaled = TimeSeriesScalerMinMax().fit_transform(X)
print(X_scaled)

# Training a Model: K-Nearest Neighbors Time-Series Classifier
from tslearn.neighbors import KNeighborsTimeSeriesClassifier
knn = KNeighborsTimeSeriesClassifier(n_neighbors=1)
knn.fit(X_scaled, y)
print(knn.predict(X_scaled))