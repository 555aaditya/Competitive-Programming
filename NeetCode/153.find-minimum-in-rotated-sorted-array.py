#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1

        while l < r:
            m = (l+r)//2
            if nums[m]>nums[r]:
                l = m+1
            else:
                r = m
        return nums[l]       
# @lc code=end