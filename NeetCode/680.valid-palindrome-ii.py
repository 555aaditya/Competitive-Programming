#
# @lc app=leetcode id=680 lang=python3
#
# [680] Valid Palindrome II
#

# @lc code=start
class Solution:
    def validPalindrome(self, s: str) -> bool:
        l=0
        r=len(s)-1
        while l<r:
            if s[l]!=s[r]:
                s_l=s[:l]+s[l+1:]
                s_r=s[:r]+s[r+1:]
                if s_l==s_l[::-1] or s_r==s_r[::-1]:
                    return True
                else:
                    return False
            else:
                l+=1
                r-=1
        return True 
        
# @lc code=end

