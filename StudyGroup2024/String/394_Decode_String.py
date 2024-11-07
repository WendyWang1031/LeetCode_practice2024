"""
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], 
where the encoded_string inside the square brackets is being repeated exactly k times. 
Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, 
square brackets are well-formed, etc. Furthermore, 
you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. 
For example, there will not be input like 3a or 2[4].

The test cases are generated so that the length of the output will never exceed 105.

 

Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"
Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"
Example 3:

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
 

Constraints:

1 <= s.length <= 30
s consists of lowercase English letters, digits, and square brackets '[]'.
s is guaranteed to be a valid input.
All the integers in s are in the range [1, 300].
"""

class Solution:
    def decodeString(self, s: str) -> str:
        count_stack = []     # 儲存重複次數的堆疊
        string_stack = []    # 儲存部分字串的堆疊
        current_string = ""  # 當前解碼字串
        current_num = 0      # 當前的重複次數
        
        for char in s:
            if char.isdigit():
                # 構建重複次數，例如 '23' 構建為 23
                current_num = current_num * 10 + int(char)
            elif char == '[':
                # 開始一個新的部分，壓入當前數字和字串
                count_stack.append(current_num)
                string_stack.append(current_string)
                # 重置當前字串和數字
                current_string = ""
                current_num = 0
            elif char == ']':
                # 結束一個部分，彈出重複次數，並生成部分解碼字串
                repeat_count = count_stack.pop()
                last_string = string_stack.pop()
                # 用 current_string * repeat_count 生成解碼的子字串，並與上一層的字串 last_string 拼接
                current_string = last_string + current_string * repeat_count
            else:
                # 將字符加到當前字串
                current_string += char

        return current_string       


#########################################################


    def decodeString_recursive(self, s: str) -> str:
        def decode(index):
            result = ""
            num = 0
            
            while index < len(s):
                char = s[index]
                
                if char.isdigit():
                    # 構建重複次數，例如 '23' 構建為 23
                    num = num * 10 + int(char)
                elif char == '[':
                    # 遞迴解析內部字串，直接忽略索引
                    decoded_string = decode(index + 1)
                    # 重複並添加到結果
                    result += decoded_string * num
                    num = 0  # 重置重複次數
                elif char == ']':
                    # 返回當前層的結果
                    return result
                else:
                    # 添加正常的字符
                    result += char
                
                index += 1
            
            return result

        # 直接獲取結果
        return decode(0)