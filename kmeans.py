import math
import pandas as pd
import matplotlib.pyplot as plt

def euclidean_distance(p1, p2):
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(p1, p2)))

def k_means_clustering(data, k, max_iter=100):
    centroids = data[:k]
    for _ in range(max_iter):
        labels = [min(range(k), key=lambda i: euclidean_distance(point, centroids[i])) for point in data]
        new_centroids = [
            [sum(point[dim] for point in cluster) / len(cluster) for dim in range(len(data[0]))]
            if (cluster := [data[j] for j in range(len(data)) if labels[j] == i]) else centroids[i]
            for i in range(k)
        ]
        if new_centroids == centroids:
            break
        centroids = new_centroids
    return labels, centroids

def plot_clusters(data, labels, centroids):
    plt.figure(figsize=(8, 6))
    for i in range(max(labels) + 1):
        cluster_points = [data[j] for j in range(len(data)) if labels[j] == i]
        if cluster_points:
            x, y = zip(*cluster_points)
            plt.scatter(x, y, label=f'Cluster {i + 1}')
    cx, cy = zip(*centroids)
    plt.scatter(cx, cy, color='red', marker='X', s=100, label='Centroids')
    plt.title('K-means Clustering')
    plt.xlabel('x coordinate')
    plt.ylabel('y coordinate')
    plt.legend()
    plt.grid()
    plt.show()

# Load data from CSV
data = pd.read_csv('exp9.csv').values.tolist()
k = int(input("Enter the number of clusters: "))

# Run K-means and plot results
labels, centroids = k_means_clustering(data, k)
print("\nFinal clusters and centroids:")
for i in range(k):
    print(f"Cluster {i + 1}: {[data[j] for j in range(len(data)) if labels[j] == i]}")
print("Final centroids:", centroids)
plot_clusters(data, labels, centroids)
