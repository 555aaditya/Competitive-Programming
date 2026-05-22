#
# @lc app=leetcode id=1768 lang=python3
#
# [1768] Merge Strings Alternately
#

# @lc code=start
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l,r = 0, 0
        _s = ""
        for i in range(len(word1)+len(word2)):
            if l<len(word1):
                _s+=word1[l]
                l+=1
            if r<len(word2):
                _s+=word2[r]
                r+=1
        return _s        
# @lc code=end

