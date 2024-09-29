'''
Brute-force 暴力破解

此代码实现了 TSP 的暴力求解方法，适用于小规模的城市数量，因为它的时间复杂度为 O(n!)，对于较大的数据集会变得非常不高效。
旅行商问题是 NP-hard 的经典问题，因此在实际应用中，通常会选择更高效的启发式或近似算法来处理大型数据集。
'''
from itertools import permutations

#计算总距离的函数
def calculate_total_distance(route, distance_matrix):
    total_distance = 0
    n = len(route)
    for i in range(n - 1):
        total_distance += distance_matrix[route[i]][route[i + 1]]
    total_distance += distance_matrix[route[-1]][route[0]]  # 返回起始城市
    return total_distance

#暴力求解 TSP 的函数
def tsp_brute_force(distance_matrix):
    n = len(distance_matrix)
    cities = list(range(n))
    min_distance = float('inf')
    best_route = None

    for perm in permutations(cities[1:]):
        route = [0] + list(perm)
        total_distance = calculate_total_distance(route, distance_matrix)

        if total_distance < min_distance:
            min_distance = total_distance
            best_route = route
    return best_route, min_distance

#定义了一个示例距离矩阵，其中每个元素表示城市之间的距离。
distance_matrix = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

#调用 tsp_brute_force 函数，找到最佳路线和最小距离，并打印结果。
best_route, min_distance = tsp_brute_force(distance_matrix)
print("Optimal route:", best_route)
print("Minimum distance:", min_distance)
