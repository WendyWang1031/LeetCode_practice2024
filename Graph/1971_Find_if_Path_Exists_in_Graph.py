"""
There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1 (inclusive). 
The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi. 
Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.

You want to determine if there is a valid path that exists from vertex source to vertex destination.

Given edges and the integers n, source, 
and destination, return true if there is a valid path from source to destination, or false otherwise.

 

Example 1:


Input: n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2
Output: true
Explanation: There are two paths from vertex 0 to vertex 2:
- 0 → 1 → 2
- 0 → 2
Example 2:


Input: n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination = 5
Output: false
Explanation: There is no path from vertex 0 to vertex 5.
 

Constraints:

1 <= n <= 2 * 105
0 <= edges.length <= 2 * 105
edges[i].length == 2
0 <= ui, vi <= n - 1
ui != vi
0 <= source, destination <= n - 1
There are no duplicate edges.
There are no self edges.
"""

from collections import defaultdict

class Solution:
    def validPath(self, n, edges, source, destination):
        # 構建鄰接表
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # 訪問過的節點
        visited = set()
        
        def dfs(node):
            # 如果當前節點就是目標節點，返回 True
            if node == destination:
                return True
            visited.add(node)  # 標記當前節點為已訪問
            
            # 遍歷當前節點的鄰居
            for neighbor in graph[node]:
                if neighbor not in visited:  # 如果鄰居未訪問過
                    # 遞迴訪問鄰居，並檢查是否能到達目標
                    if dfs(neighbor):  
                        return True
            # 如果所有鄰居都無法到達目標，返回 False
            return False
        
        # 從 source 節點開始執行 DFS
        return dfs(source)

# 測試用例
solution = Solution()
n = 6
edges = [[0,1], [0,2], [2,3], [2,4], [4,5]]
source = 0
destination = 5
result = solution.validPath(n, edges, source, destination)
print(result)  # Output: True