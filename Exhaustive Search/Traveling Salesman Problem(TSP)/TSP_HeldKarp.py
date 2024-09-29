'''
Held-Karp algorithm

使用记忆来存储中间结果，将时间复杂度降低到 O(n2 * 2n)。但是，对于较大的 n 来说，这仍然不可行。

This method involves breaking the problem into smaller subproblems and solving each subproblem only once, storing the results to avoid redundant calculations.
该方法涉及将问题分解为更小的子问题，并且每个子问题只解决一次，存储结果以避免重复计算。

Step-by-Step Implementation:
Define the Problem: Represent the cities and the distances between them using a distance matrix.定义问题：使用距离矩阵表示城市及其之间的距离。
Initialize the Dynamic Programming Table: Create a table to store the minimum costs of visiting subsets of cities.初始化动态规划表：创建一个表来存储访问城市子集的最低成本。
Iterate Through Subsets: Compute the minimum costs for visiting subsets of cities and update the table.迭代子集：计算访问城市子集的最低成本并更新表格。
Compute the Optimal Path: Reconstruct the optimal path from the dynamic programming table.计算最佳路径：从动态规划表重建最佳路径。
'''
n = 4  # there are four nodes in example graph (graph is 1-based)

# dist[i][j] represents shortest distance to go from i to j
# this matrix can be calculated for any given graph using
# all-pair shortest path algorithms
dist = [[0, 0, 0, 0, 0], [0, 0, 10, 15, 20], [
        0, 10, 0, 25, 25], [0, 15, 25, 0, 30], [0, 20, 25, 30, 0]]

# memoization for top down recursion
memo = [[-1]*(1 << (n+1)) for _ in range(n+1)]


def fun(i, mask):
    # base case
    # if only ith bit and 1st bit is set in our mask,
    # it implies we have visited all other nodes already
    if mask == ((1 << i) | 3):
        return dist[1][i]

    # memoization
    if memo[i][mask] != -1:
        return memo[i][mask]

    res = 10**9  # result of this sub-problem

    # we have to travel all nodes j in mask and end the path at ith node
    # so for every node j in mask, recursively calculate cost of
    # travelling all nodes in mask
    # except i and then travel back from node j to node i taking
    # the shortest path take the minimum of all possible j nodes
    for j in range(1, n+1):
        if (mask & (1 << j)) != 0 and j != i and j != 1:
            res = min(res, fun(j, mask & (~(1 << i))) + dist[j][i])
    memo[i][mask] = res  # storing the minimum value
    return res


# Driver program to test above logic
ans = 10**9
for i in range(1, n+1):
    # try to go from node 1 visiting all nodes in between to i
    # then return from i taking the shortest route to 1
    ans = min(ans, fun(i, (1 << (n+1))-1) + dist[i][1])

print("The cost of most efficient tour = " + str(ans))

# This code is contributed by Serjeel Ranjan
