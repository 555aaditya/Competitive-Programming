#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        freq = {}
        for num in s:
            freq[num] = freq.get(num,0)+1
        for num in t:
            freq[num] = freq.get(num,0)-1
            if freq[num] < 0:
                return False
        return True
# @lc code=end