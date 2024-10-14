"""
Given an array of strings strs, group the anagrams together. 
You can return the answer in any order.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]

"""

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dict = {}
        
        for word in strs:
            sorted_words = ''.join(sorted(word))

            if sorted_words in dict:
                dict[sorted_words].append(word)
            else:
                dict[sorted_words] = [word]

        return list(dict.values())
    
solution = Solution()
strs1 = ["eat","tea","tan","ate","nat","bat"]
result = solution.groupAnagrams(strs1)
print(result)