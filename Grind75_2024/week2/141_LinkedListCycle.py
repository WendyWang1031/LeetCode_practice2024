"""
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. 
Internally, pos is used to denote the index of the node that tail's next pointer is connected to. 
Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

 

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

Example 2:
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

Example 3:
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
 

Constraints:

The number of the nodes in the list is in the range [0, 104].
-105 <= Node.val <= 105
pos is -1 or a valid index in the linked-list.

"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle_hash(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        visited = set()
        while head:
            if head in visited:
                return True
            visited.add(head)
            head = head.next
        return False
    
    def hasCycle_twoPointers(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow , fast = head , head
        while fast and fast.next :  # 當 fast 及其下一個節點存在時繼續迴圈
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
"""
雙指針法被視為最佳解，因為其時間和空間效率都優於 Hash Set 法：

時間複雜度：兩種方法都是 O(n)。
空間複雜度：
雙指針法為 O(1)，僅使用了兩個指針。
Hash Set 法為 O(n)，需要記錄每個節點的位置。
"""