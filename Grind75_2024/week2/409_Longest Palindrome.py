"""
Given a string s which consists of lowercase or uppercase letters, return the length of the longest 
palindrome
 that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome.

 

Example 1:
Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.

Example 2:
Input: s = "a"
Output: 1
Explanation: The longest palindrome that can be built is "a", whose length is 1.

不必在乎構成的具體順序，而是關注可以使用的字母數量和出現次數。
所有出現偶數次的字母都可以完整地被加入回文中。
出現奇數次的字母可以被加入最大偶數次，而只能有一個字母允許在回文中心出現一次（即中心的字母，可以保留一個單次字母）。
"""
from collections import Counter

class Solution(object):
    def longestPalindrome_hashmap(self, s):
        """
        :type s: str
        :rtype: int
        """
        counter = Counter(s)
        length = 0
        odd_found = False

        for char_count in counter.values():
            if char_count % 2 == 0 :
                length += char_count
            else:
                length += char_count - 1 # 奇數次數，加入最大偶數部分（即次數減 1）
                odd_found = True
        if odd_found:
            length += 1
        return length
    
    def longestPalindrome_set(self, s):
        """
        :type s: str
        :rtype: int
        """
        odd_chars = set()
        length = 0

        for char in s:
            if char in odd_chars:
                odd_chars.remove(char)
                length += 2

            else:
                odd_chars.add(char)
        if odd_chars:
            length += 1
        return length
