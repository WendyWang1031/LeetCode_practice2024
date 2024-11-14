"""
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

 

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false

Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true

ransomNote 代表想要撰寫的勒索信字母組合，
而 magazine 代表可用來拼湊勒索信的字母來源。是magazine 是被拿來當源頭來使用！！
我們的任務是確保 magazine 中的字母數量足以構成 ransomNote。
 
"""
from collections import Counter

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        # 計算每個字母的出現次數
        ransom_count = Counter(ransomNote)
        magazine_count = Counter(magazine)

        # 遍歷 ransomNote 的每個字母，確認 magazine 是否有足夠的數量
        for char , count in ransom_count.items():
            if magazine_count[char] < count:
                return False
        return True
    
"""
當遍歷字典，且需要鍵和值時，用 items()。
當遍歷列表或字串並且需要索引值時，用 enumerate()。

時間複雜度：O(m + n)，其中 m 和 n 分別是 ransomNote 和 magazine 的長度。這是因為計數哈希表需要遍歷兩個字串的每個字母。
空間複雜度：O(k)，其中 k 是 magazine 中不同字母的數量。我們需要一個哈希表來存儲 magazine 的字母計數。
"""