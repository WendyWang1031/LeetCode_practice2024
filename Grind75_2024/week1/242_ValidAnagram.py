"""
Given two strings s and t, return true if t is an 
anagram of s, and false otherwise.


Example 1:

Input: s = "anagram", t = "nagaram"
Output: true

Example 2:

Input: s = "rat", t = "car"
Output: false

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.

"""

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        count_s = {}
        count_t = {}

        for char in s:
            count_s[char] = count_s.get(char , 0) + 1
        for char in t:
            count_t[char] = count_t.get(char , 0) + 1

        return count_s == count_t
    
"""
Complexity
Time Complexity: O(N)
Space Complexity: O(N)
"""