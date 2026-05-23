#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l,r = 0, len(height)-1
        _a = 0
        _h = 0
        _w = 0
        while l<r:
            _h = min(height[l],height[r])
            _w = r-l
            _a = max(_a,_h*_w)
            if height[l]>height[r]:
                r-=1
            else:
                l+=1
        return _a
# @lc code=end

