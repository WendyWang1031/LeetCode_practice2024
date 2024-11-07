"""
Given the root of a binary tree, 
check whether it is a mirror of itself (i.e., symmetric around its center).

Example 1:
Input: root = [1,2,2,3,4,4,3]
Output: true

Example 2:
Input: root = [1,2,2,null,3,null,3]
Output: false
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val # 當前節點的值
        self.left = left # 左子節點
        self.right = right # 右子節點

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root :
            return True
        
        def isMirror(left,right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            return(left.val == right.val and
                   isMirror(left.left , right.right) and
                   isMirror(left.right , right.left)
                   )
        return isMirror(root.left , root.right)

# 測試
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(4)
root.right.right = TreeNode(3)

solution = Solution()
print(solution.isSymmetric(root))



    
    