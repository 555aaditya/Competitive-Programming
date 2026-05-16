#
# @lc app=leetcode id=624 lang=python3
#
# [624] Maximum Distance in Arrays
#

# @lc code=start
class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        _min = int('inf')
        _max = int('-inf')

        for i in range(len(arrays)):
            _min = min(_min,arrays[i][0])
            _max = max(_max,arrays[i][-1])
        return _max-_min
# @lc code=end

