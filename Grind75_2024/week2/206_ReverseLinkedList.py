"""
Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [1,2]
Output: [2,1]
Example 3:

Input: head = []
Output: []

"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        prev = None
        current = head

        while current is not None:
            next_node = current.next # 儲存下一個節點
            current.next = prev # 反轉

            prev = current
            current = next_node

        return prev
    
"""

這樣每次迴圈就將當前節點的 next 指向前一個節點，逐步反轉整個鏈表。
這種解法的時間複雜度為 O(n)，空間複雜度為 O(1)。
"""