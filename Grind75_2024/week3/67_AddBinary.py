"""
Given two binary strings a and b, return their sum as a binary string.

Example 1:
Input: a = "11", b = "1"
Output: "100"

Example 2:
Input: a = "1010", b = "1011"
Output: "10101"
 

Constraints:

1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.
"""
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        s = []
        carry = 0
        i = len(a) - 1
        j = len(b) - 1
        
        while i >= 0 or j >= 0 or carry:
            if i >= 0:
                carry += int(a[i])
                i -= 1
            if j >= 0:
                carry += int(b[j])
                j -= 1
            s.append(str(carry % 2)) # 結果位 = carry % 2
            carry //= 2 # 更新 carry 為進位位

        return ''.join(reversed(s))

"""
時間複雜度：O(max(len(a), len(b)))，因為我們從右到左遍歷兩個字串。
空間複雜度：O(max(len(a), len(b)))，因為我們儲存每一位的結果，最終需要反轉。
"""

