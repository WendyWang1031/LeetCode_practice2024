"""
Given a binary tree, determine if it is 
height-balanced
.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: true

Example 2:
Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
Example 3:

Input: root = []
Output: true

Constraints:
The number of nodes in the tree is in the range [0, 5000].
-104 <= Node.val <= 104
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        return self.check_balance(root) != -1
    def check_balance(self, node):
        if node is None:
            return 0
        
        left_depth = self.check_balance(node.left)
        if left_depth == -1:
            return -1
        right_depth = self.check_balance(node.right)
        if right_depth == -1:
            return -1
        
        if abs(left_depth-right_depth) > 1:
            return -1
        
        return max(left_depth , right_depth) +1

"""
所以分別是計算左右兩邊的深度
從最底部開始計算取最大值節點，然後再去比較左邊減右邊的絕對值
如果大於1 就等於不平衡

時間複雜度：O(n)，其中 n 是節點數量。每個節點最多被訪問一次，計算它的深度或檢查平衡性。
空間複雜度：O(h)，其中 h 是樹的高度。遞迴調用的深度最多到達樹的高度。
"""        
        
        
        

