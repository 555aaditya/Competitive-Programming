#
# @lc app=leetcode id=189 lang=python3
#
# [189] Rotate Array
#

# @lc code=start
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        def reverse(low, high):
            while low<high:
                nums[low], nums[high] = nums[high], nums[low]
                low+=1
                high-=1

        l, r, k = 0, len(nums)-1, k%len(nums)
        reverse(l,r)
        reverse(l,k-1)
        reverse(k,r)        
        
# @lc code=end

