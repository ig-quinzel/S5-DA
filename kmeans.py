import math

import pandas as pd

import matplotlib.pyplot as plt

def euclidean_distance(point1, point2):
 return math.sqrt(sum((a-b)**2 for a,b in zip(point1,point2)))

def k_means_clustering(data,k,max_iterations =100):
 centroids = data[:k]
 for iteration in range(max_iterations): 
  labels=[min(range(k),key=lambda i: euclidean_distance(point,centroids[i])) for point in data]
  new_centroids =[]
  for i in range(k): 
   cluster_points = [data[j] for j in range(len(data)) if labels[j] ==i]
   if len(cluster_points)>0:
     new_centroid = [sum(point[dim] for point in cluster_points)/ len(cluster_points) for dim in range(len(data[0]))] 
     new_centroids.append(new_centroid)
   else:
     new_centroids.append(centroids[i])
  print(f"Iteration {iteration + 1} clusters:")
  for i in range(k):
    cluster_points = [data[j] for j in range(len(data)) if labels[j]==i]
    print(f"Cluster {i+1}:{cluster_points}")
  if new_centroids==centroids:
    break
  else:
   centroids= new_centroids
 return labels, centroids

def plot_clusters(data,labels,centroids): 
  plt.figure(figsize =(8,6))
  for i in range(max(labels) + 1):
    cluster_points = [data[j] for j in range(len(data)) if labels[j] == i] 
    cluster_points=list(zip(*cluster_points)) 
    plt.scatter(cluster_points[0], cluster_points[1], label=f'Cluster{i+1}')
  centroids_x, centroids_y = zip(*centroids)
  plt.scatter(centroids_x, centroids_y, color='red', marker='X', s=100, label= 'Centroids')
  plt.title('K-means Clustering') 
  plt.xlabel('x cordinate')
  plt.ylabel('y cordinate') 
  plt.legend()
  plt.grid()
  plt.show()

csv_file='exp9.csv'
df = pd.read_csv(csv_file)
data = df.values.tolist()
k=int(input("Enter the number of clusters: "))
labels, centroids = k_means_clustering(data, k)

print("\nFinal clusters are:") 
for i in range(k):
 cluster_points=[data[j] for j in range(len(data)) if labels[j] == i] 
 print(f"Cluster{i + 1} : {cluster_points}")
print("Final centroids are.")
print(centroids)
plot_clusters(data, labels, centroids)
