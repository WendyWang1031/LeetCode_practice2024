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
"""

class Solution1(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dict_map = {
            '(':')',
            '[':']',
            '{':'}'
        }
        stack = []

        for char in s:
            if char in dict_map:
                stack.append(dict_map[char])
            else:
                if len(stack) == 0:
                    return False
                top_element = stack.pop()
                if top_element != char:
                    return False
        return len(stack) == 0
    
# solution1 = Solution1()
# s1 = "({[})]"
# result = solution1.isValid(s1)
# print(result)

class Solution3(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d = {'(':')', '{':'}','[':']'}
        stack = []
        for i in s:
            if i in d:  # 1
                stack.append(i)
            elif len(stack) == 0 or d[stack.pop()] != i:  # 2
                return False
        return len(stack) == 0 # 3


class Solution2(object):
    def isValid(self, s: str) -> bool: 
        # 使用 stack 來幫助做配對檢查 
        # 宣告一個可以 mapping 檢查的 map
        stack = [] 
        bracket_map = {'(': ')', '[': ']', '{': '}'} 

        for char in s: 
            if char in bracket_map: 
                stack.append(char) 
            else: 
                # 檢查當前遇到的閉括號是否和堆疊中最後一個開括號相匹配
                # 其實就是要藉由這個Stack去確認順序
                if not stack or bracket_map[stack.pop()] != char: 
                    return False 
        return len(stack) == 0 

 
solution2 = Solution2()
s1 = "({[})]"
result1 = solution2.isValid(s1)
print(result1)

s2 = ")("
result2 = solution2.isValid(s2)
print(result2)

s3 = "()[]{}"
result3 = solution2.isValid(s3)
print(result3)