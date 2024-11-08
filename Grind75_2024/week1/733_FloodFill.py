"""
You are given an image represented by an m x n grid of integers image, 
where image[i][j] represents the pixel value of the image. 
You are also given three integers sr, sc, and color. 
Your task is to perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill:

Begin with the starting pixel and change its color to color.
Perform the same process for each pixel that is directly adjacent 
(pixels that share a side with the original pixel, either horizontally or vertically)
and shares the same color as the starting pixel.
Keep repeating this process by checking neighboring pixels of the updated pixels and modifying their color 
if it matches the original color of the starting pixel.
The process stops when there are no more adjacent pixels of the original color to update.
Return the modified image after performing the flood fill.

 

Example 1:

Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2

Output: [[2,2,2],[2,2,0],[2,0,1]]

From the center of the image with position (sr, sc) = (1, 1) 
(i.e., the red pixel), all pixels connected by a path of the same color as the starting pixel
(i.e., the blue pixels) are colored with the new color.

Note the bottom corner is not colored 2, 
because it is not horizontally or vertically connected to the starting pixel.

Example 2:

Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0

Output: [[0,0,0],[0,0,0]]

Explanation:

The starting pixel is already colored with 0, 
which is the same as the target color. Therefore, no changes are made to the image.
"""
# 使用DFS解
class Solution_dfs:
    def floodFill(self, image, sr, sc, color):
        originalColor = image[sr][sc]
        
        # 如果起始點的顏色已經是 newColor，直接返回，避免無限遞迴
        if originalColor == color:
            return image
        
        def dfs(r, c):
            # 若座標超出邊界或顏色不匹配，直接返回
            if r < 0 or r >= len(image) or c < 0 or c >= len(image[0]) or image[r][c] != originalColor:
                return
            
            # 修改當前位置的顏色
            image[r][c] = color
            
            # 對四個方向進行遞迴填色
            dfs(r + 1, c)  # 向下
            dfs(r - 1, c)  # 向上
            dfs(r, c + 1)  # 向右
            dfs(r, c - 1)  # 向左
        
        # 從起始點開始填色
        dfs(sr, sc)
        return image

# 使用 bfs 解
from collections import deque
class Solution_bfs(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        original_color = image[sr][sc]
        if original_color == color:
            return image
        queue = deque([(sr,sc)])

        while queue:
            r,c = queue.popleft()

            if image[r][c] == original_color:
                image[r][c] = color

            for dr,dc in [(1,0) , (-1,0), (0,1) , (0,-1)]:
                nr , nc = r+dr , c+dc
                if 0 <= nr < len(image) and 0 <= nc < len(image[0]) and image[nr][nc] == original_color:
                    queue.append((nr,nc))
        return image
    

"""
兩者都是：

時間複雜度：O(NxM)
其中 
N 是 image 的行數，
M 是列數。每個點最多訪問一次。

空間複雜度：
O(NxM) 遞迴深度或隊列的大小在最壞情況下需要包含所有點。
"""