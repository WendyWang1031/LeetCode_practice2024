"""
3. Longest Substring Without Repeating Characters
Given a string s, find the length of the longest 
substring
 without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""
class Solution(object):
    def lengthOfLongestSubstring_worst(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_length = 0  # 儲存目前找到的最大長度

        # 外層迴圈：遍歷每個起始點
        for i in range(len(s)):
            seen_chars = set()  # 儲存當前子串中的字符
            current_length = 0  # 當前子串的長度
            
            # 內層迴圈：從當前起始點向後檢查每個字符
            for j in range(i, len(s)):
                if s[j] in seen_chars:
                    break  # 若出現重複字符，結束當前子串的檢查
                
                seen_chars.add(s[j])  # 加入當前字符
                current_length += 1  # 增加當前子串的長度
            
            # 更新最大長度
            max_length = max(max_length, current_length)
        
        return max_length
    

#########################################################    
   
   
    def lengthOfLongestSubstring_best(self, s):
        # 儲存每個字符最後出現的位置
        char_map = {}
        max_length = 0
        start = 0 # 滑動窗口的起始位置
        
        for i ,char in enumerate(s):
            # 若字符重複，並且重複字符的位置在當前窗口內
            
            # 說明這個字符已經在當前窗口中出現過，
            # 則我們需要將窗口的左邊界 start 移動到這個重複字符的下一個位置，
            # 以保持窗口內無重複字符。
            if char in char_map and char_map[char] >= start:
                # 將窗口起點移動到重複字符的下一位置
                start = char_map[char] + 1
            
            # 更新字符最後一次出現的位置
            char_map[char] = i
            # 計算當前窗口的長度並更新最大長度
            max_length = max(max_length , i - start + 1)

        return max_length



