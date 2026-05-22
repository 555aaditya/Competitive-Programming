#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int):
        l,r=0,0
        _ans = []
        for i in range(m+n):
            if l>=m:
                _ans.append(nums2[r])
                r+=1
            elif r>=n:
                _ans.append(nums1[l])
                l+=1
            elif nums1[l]>=nums2[r]:
                _ans.append(nums2[r])
                r+=1
            else:
                _ans.append(nums1[l])
                l+=1
        
        for i in range(m+n):
            nums1[i] = _ans[i]        
# @lc code=end

