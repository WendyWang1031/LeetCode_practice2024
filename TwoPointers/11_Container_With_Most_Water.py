"""
You are given an integer array height of length n. 
There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, 
such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

 

Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.


Example 2:
Input: height = [1,1]
Output: 1
 

Constraints:

n == height.length
2 <= n <= 105
0 <= height[i] <= 104
"""

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0  # 左指針
        right = len(height) - 1  # 右指針
        max_area = 0  # 記錄最大容積
        
        # 當左指針和右指針未相遇時
        while left < right:
            # 計算當前容積
            width = right - left  # 寬度是兩個指針之間的距離
            min_height = min(height[left], height[right])  # 高度是兩條線段中較短的那條
            current_area = width * min_height  # 容積 = 寬度 × 高度
            
            # 更新最大容積
            max_area = max(max_area, current_area)
            
            # 移動指針，移動較短的那一條
            if height[left] < height[right]:
                left += 1  # 如果左邊較短，移動左指針
            else:
                right -= 1  # 如果右邊較短，移動右指針
        
        return max_area  # 返回最大容積
