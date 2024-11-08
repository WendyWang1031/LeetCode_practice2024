"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. 
The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

 

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:

Input: list1 = [], list2 = []
Output: []

Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
 

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode()
        current = dummy #建立一個指針（current）：從 dummy 開始，用於追蹤和連接新的鏈結節點。

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next # 移動 list1 到下一個節點
            else:
                current.next = list2
                list2 = list2.next
            current = current.next # 移動 current 指針到下一個節點
        current.next = list1 if list1 else list2
        return dummy.next # 返回合併後的鏈結串列，排除虛擬頭節點

"""
時間複雜度：
O(n+m)，其中 
n 和 m 是 list1 和 list2 的長度。

空間複雜度：
O(1)，因為我們使用了現有的節點，只分配了常數空間。
"""