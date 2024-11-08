"""
Given a binary search tree (BST), 
find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: 
“The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants 
(where we allow a node to be a descendant of itself).”

Example 1:

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.

Example 2:

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, 
since a node can be a descendant of itself according to the LCA definition.

Example 3:

Input: root = [2,1], p = 2, q = 1
Output: 2
 

Constraints:

The number of nodes in the tree is in the range [2, 105].
-109 <= Node.val <= 109
All Node.val are unique.
p != q
p and q will exist in the BST.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor_binaryTree(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        while root:
            if p.val < root.val and q.val < root.val:
                root = root.left
            elif p.val > root.val and q.val > root.val:
                root = root.right
            else:
                return root
            

    def lowestCommonAncestor_dfs(self, root, p, q):
        if not root or root == p or root == q:
            return root
        
        left = self.lowestCommonAncestor_dfs(root.left,p,q)
        right = self.lowestCommonAncestor_dfs(root.right,p,q)

        if left and right:
            return root
        return left if left else right

"""
Binary Search Tree
時間複雜度：O(logN)（平均情況下，對於平衡的二元搜尋樹），最壞情況為 O(N)，例如當樹退化為鏈表時。
空間複雜度：O(1)（迭代版本）或 O(logN)（遞迴版本的棧空間）。

DFS
時間複雜度：O(N)，因為可能需要遍歷整棵樹。
空間複雜度：O(N)（最壞情況下遞迴棧的空間複雜度）。
"""