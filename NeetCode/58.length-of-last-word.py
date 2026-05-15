#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        cnt = 0
        n = len(s)
        for n in range(n-1,-1,-1):
            if s[n]!=" ":
                cnt+=1
            elif cnt>0:
                break
        return cnt 
# @lc code=end

