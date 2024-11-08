"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true

Example 2:

Input: s = "()[]{}"
Output: true

Example 3:

Input: s = "(]"
Output: false

Example 4:

Input: s = "([])"
Output: true

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""

class Solution(object):
    def isValid(self, s): 
        stack = []
        bracket_map = {
            "(":")",
            "[":"]",
            "{":"}"
        }
        for char in s :
            if char in bracket_map :
                stack.append(char)
            else:
                if not stack and bracket_map[stack.pop()] != char:
                    return False
        return True
    
"""
時間複雜度：O(n)，因為我們需要遍歷整個字符串，每個字符的操作（推入和彈出堆疊）都是 O(1)。
空間複雜度：O(n)，因為在最壞情況下，堆疊需要存儲最多 n 個開括號。
"""