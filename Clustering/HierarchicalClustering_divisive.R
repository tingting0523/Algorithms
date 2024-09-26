#install.packages("cluster")
library(cluster)

# 创建学生的学习数据集
students_data <- data.frame(
  exam_scores = c(85, 78, 90, 88, 76, 95, 60, 92, 74, 82),
  assignment_quality = c(90, 85, 93, 88, 76, 95, 60, 90, 70, 80),
  class_participation = c(80, 70, 95, 85, 65, 90, 50, 85, 60, 75)
)

# 打印数据集
print(students_data)

# 计算欧几里得距离矩阵
dist_matrix <- dist(students_data, method = "euclidean")
print(dist_matrix)

# 进行DIANA聚类
diana_result <- diana(dist_matrix)

# 查看聚类结果的结构
print(diana_result)

# 绘制树状图
#plot(diana_result, main = "DIANA Clustering Dendrogram for Students")
# 绘制仅树状图
plot(as.hclust(diana_result), main = "DIANA Clustering Dendrogram for Students")

# 打印每个簇的成员
print(cutree(as.hclust(diana_result), k = 2))  # 分成两类

