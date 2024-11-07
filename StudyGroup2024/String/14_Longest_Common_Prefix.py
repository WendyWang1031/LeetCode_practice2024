"""
14. Longest Common Prefix
Easy
Topics
Companies
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.

"""

class Solution(object):
    # 普通解
    def longestCommonPrefix_worst(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        if not strs:
            return ""
        
        # 找到最短字串的長度，避免越界
        min_length = min(len(s) for s in strs)
        
        # 遍歷每個字符位置，最多到最短字串的長度
        for i in range(min_length):
            char = strs[0][i]  # 取第一個字串的當前字符
            for s in strs[1:]:  # 比較其他字串
                if s[i] != char:
                    return strs[0][:i]  # 字符不匹配，返回當前累積的前綴
    
        # 如果遍歷完所有字符，說明全部匹配
        return strs[0][:min_length]
    

#########################################################  
  
    # 熱門解
    def longestCommonPrefix_best(self, strs):
        if not strs:
            return ""
        
        # 找到字串中最短的字串，這樣可以減少不必要的比較
        prefix = min(strs , key=len)

        # 外層迴圈遍歷最短字串的每個字符
        for i in range(len(prefix)):
            char = prefix[i]
            
            # 內層迴圈檢查每個字串在該位置的字符是否與最短字串的字符相同
            for s in strs:
                
                # 如果當前字符位置的字符不匹配，返回到目前為止的共同前綴
                if s[i] != char:
                    return prefix[:i]
        return prefix


#########################################################    


    # 其一最佳解
    def longestCommonPrefix_py(self, strs) -> str:
        
        pre = strs[0]
        
        for i in strs:
            while not i.startswith(pre):
                pre = pre[:-1]
        
        return pre
    

######################################################### 

def longestCommonPrefix_bisection(strs):
    # 如果字串列表為空，則返回空字串
    if len(strs) == 0:
        return ""
    
    # 找到字串中最短字串的長度，這樣可以避免超出最短字串的長度
    min_length = min(len(string) for string in strs)
    
    # 設定二分法的左右邊界
    left = 0
    right = min_length
    
    # 二分搜索範圍內的最長共同前綴
    while left <= right:
        mid = (left + right) // 2  # 計算中間位置
        
        # 檢查所有字串的前 mid 個字符是否一致
        is_common_prefix = True
        for string in strs:
            if string[:mid] != strs[0][:mid]:  # 若有字串前 mid 個字符不一致
                is_common_prefix = False
                break
        
        # 若前 mid 個字符一致，嘗試更長的範圍
        if is_common_prefix:
            left = mid + 1
        else:  # 若前 mid 個字符不一致，縮短範圍
            right = mid - 1
    
    # 返回最長的共同前綴，長度為 right
    return strs[0][:right]


solution = Solution()
strs1 = ["flower","flow","flight"]
strs2 = ["dog","racecar","car"]
result_worst1 = solution.longestCommonPrefix_worst(strs1)
result_worst2 = solution.longestCommonPrefix_worst(strs2)
result_best1 = solution.longestCommonPrefix_best(strs1)
result_best2 = solution.longestCommonPrefix_best(strs2)
result_py1 = solution.longestCommonPrefix_py(strs1)
result_py2 = solution.longestCommonPrefix_py(strs2)
print(result_worst1)
print(result_worst2)
print(result_best1)
print(result_best2)
print(result_py1)
print(result_py2)