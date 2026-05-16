#
# @lc app=leetcode id=2486 lang=python3
#
# [2486] Append Characters to String to Make Subsequence
#

# @lc code=start
class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        
        m,n=len(s),len(t)

        i = 0
        j = 0

        while i<m and j<n:
            if t[j]==s[i]:
                j+=1
            i+=1

        return (n-j)

# @lc code=end

