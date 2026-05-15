#
# @lc app=leetcode id=1299 lang=python3
#
# [1299] Replace Elements with Greatest Element on Right Side
#

# @lc code=start
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        _max = -1

        for i in range(n-1,-1,-1):
            new = arr[i]
            arr[i] = _max
            _max = max(_max,new)
        return arr
# @lc code=end

