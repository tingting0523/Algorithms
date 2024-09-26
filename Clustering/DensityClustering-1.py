import matplotlib.pyplot as plt     # pyplot用于绘制图形
import numpy as np
from sklearn.cluster import DBSCAN  # DBSCAN 聚类算法
from sklearn import metrics         # metrics计算评估指标，如轮廓系数
from sklearn.datasets import make_blobs  # 生成聚类数据的工具
from sklearn.preprocessing import StandardScaler
from sklearn import datasets


# Load data in X：生成 300 个样本，分为 4 个中心
X, y_true = make_blobs(n_samples=300       # X 是一个形状为 (300, 2) 的数组
					   , centers=4         # Y是一个包含真实标签的数组，标识每个样本点所属的聚类类别，值从 0 到 3，表示4个不同的中心。 定中心数量的依据可以是你对数据分布的先验知识、研究目标或试验设计。通常在聚类分析中，可以使用一些方法（如肘部法则）来确定最佳的聚类数量，但在生成数据时你可以自由设置。centers 的设置是为了生成测试数据，而密度聚类算法本身在处理真实数据时并不需要预先指定聚类数量。
					   , cluster_std=0.50  # 标准差为 0.5 ：标准差cluster_std是指数据点围绕每个中心的散布程度。标准差越小，样本点聚集得越紧密；标准差越大，样本点的分散程度越高。这里设置为 0.5 意味着每个中心周围的点会在该中心附近 0.5 的范围内分布。标准差的值通常是根据希望生成的数据分布特性来设定的。0.5 是一个较小的标准差，适合用于测试，确保聚类效果明显。你可以根据具体需求调整这个值，例如：如果想要更多的重叠，可以增大标准差。如果希望聚类更清晰，保持小的标准差。
					   , random_state=0)        

# 应用 DBSCAN 算法
db = DBSCAN(eps=0.3, min_samples=10).fit(X) # eps=0.3 邻居的最大距离 min_samples=10 核心点的最小样本数
core_samples_mask = np.zeros_like(db.labels_, dtype=bool)  # core_samples_mask 用于标识核心样本
core_samples_mask[db.core_sample_indices_] = True
labels = db.labels_

# Number of clusters in labels, ignoring noise if present. 计算聚类数量
n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)   # 计算聚类的数量，忽略噪声（标签为 -1 的样本）


# Plot result 绘制聚类结果
# Black removed and is used for noise instead.  根据聚类结果绘制散点图，使用不同颜色表示不同的聚类，黑色表示噪声。
unique_labels = set(labels)
colors = ['y', 'b', 'g', 'r']
print(colors)
for k, col in zip(unique_labels, colors):
	if k == -1:
		# Black used for noise.
		col = 'k'  # 噪声点用黑色表示

	class_member_mask = (labels == k)

	xy = X[class_member_mask & core_samples_mask]
	plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=col,
			markeredgecolor='k',
			markersize=6)

	xy = X[class_member_mask & ~core_samples_mask]
	plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=col,
			markeredgecolor='k',
			markersize=6)

plt.title('number of clusters: %d' % n_clusters_)
plt.show()


# evaluation metrics
sc = metrics.silhouette_score(X, labels)
print("Silhouette Coefficient:%0.2f" % sc)  # 计算并输出轮廓系数（Silhouette Coefficient），用于评估聚类质量，值越高表示聚类效果越好。
# ari = adjusted_rand_score(y_true, labels)
# print("Adjusted Rand Index: %0.2f" % ari)
