import numpy as np
from sklearn.cluster import KMeans

# Create the dataset
data = np.array([[1, 2], [1, 4], [2, 3], [8, 8], [9, 10], [10, 8]])
k = 2

# Initialize and fit the K-means clustering model
model = KMeans(n_clusters=k, random_state=42, n_init=10)
model.fit(data)

labels = model.labels_
centroids = model.cluster_centers_

# Display the data points, their assigned clusters, and centroids
print("Data Points and Their Clusters:")
for point, label in zip(data, labels):
    print(f"Point {point} Cluster {label + 1}")

print("\nCluster Centroids:")
print(centroids)