import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
from sklearn.datasets import make_blobs
 
# Set a random seed to ensure the reproducibility of the results.
np.random.seed(0)
 
# 使用正态分布生成三个不同的聚类（聚会组）的数据点，loc 是均值，scale 是标准差，size 是生成点的数量。
# Generate three different clusters of data points using a normal distribution, where loc is the mean
# scale is the standard deviation
# size is the number of points to generate -- Generates a two-dimensional array of shape 15 x 2
data_1 = np.random.normal(loc=9, scale=1, size=(15, 2))   
data_2 = np.random.normal(loc=12, scale=1, size=(15, 2))  
data_3 = np.random.normal(loc=20, scale=1, size=(15, 2))  
 
# create some noise data
noise = np.array([[2, 3], [3, 18], [17, 4], [22, 15]])
 
# Combine all points into a single dataset.
data = np.vstack([data_1, data_2, data_3, noise])
 
print("Original data:",data)

# 可视化原始数据点 --  使用散点图展示原始数据点  Visualize the original data points using a scatter plot.
plt.scatter(data[:, 0], data[:, 1], c='black', label='Order')
plt.xlabel('Time')
plt.ylabel('Purchase')
plt.title('')
plt.legend()
plt.show()   
 
# Set the parameters for the DBSCAN algorithm
epsilon = 6      # Radius ε: The neighborhood range of the points.  半径ε ： 点的邻域范围   
min_samples = 3  # MinPts: The minimum number of points that must be present in the neighborhood to form a cluster. MinPts：在邻域内必须包含的最小点数，以形成一个聚类 
 
# 应用DBSCAN算法：创建 DBSCAN 对象并将其应用于数据集    Apply the DBSCAN algorithm: Create a DBSCAN object and apply it to the dataset.
# define the model
dbscan = DBSCAN(eps=epsilon, min_samples=min_samples)
# train the model
dbscan.fit(data)
  
# Get the clustering results.
labels = dbscan.labels_        # -1 means noise data
 
# 可视化聚类结果：首先绘制噪声点，然后为每个聚类绘制不同颜色的点 Visualize the clustering results: plot the noise points, and then plot points for each cluster in different colors.
plt.scatter(data[labels == -1][:, 0], data[labels == -1][:, 1], c='black', label='Noise')
for i in range(max(labels) + 1):
    plt.scatter(data[labels == i][:, 0], data[labels == i][:, 1], label=f'Cluster {i + 1}')
plt.xlabel('Time')
plt.ylabel('Purchase')
plt.title('DBSCAN Clustering')
plt.legend()
plt.show()
 
# Return the clustering labels
print("labels:",labels)