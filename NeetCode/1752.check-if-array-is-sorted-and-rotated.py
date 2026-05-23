#
# @lc app=leetcode id=1752 lang=python3
#
# [1752] Check if Array Is Sorted and Rotated
#

# @lc code=start
class Solution:
    def check(self, nums: List[int]) -> bool:
        cnt = 0
        n = len(nums)
        for i in range(n):
            if nums[i]>nums[(i+1)%n]:
                cnt += 1
            if cnt > 1:
                return False
        return True
# @lc code=end

