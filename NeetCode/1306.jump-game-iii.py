#
# @lc app=leetcode id=1306 lang=python3
#
# [1306] Jump Game III
#

# @lc code=start
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        q = deque()
        visited = set()
        q.append(start)

        while q:
            indx = q.popleft()
            if arr[indx]==0:
                return True

            for i in ((indx+arr[indx]),(indx-arr[indx])):
                if 0<=i<len(arr) and i not in visited:
                    q.append(i)
                    visited.add(indx)
        return False

# @lc code=end

