#
# @lc app=leetcode id=3898 lang=python3
#
# [3898] Find the Degree of Each Vertex
#

# @lc code=start
class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        n = len(matrix)
        dgr=[]
        for i in range(n):
            cnt=0
            for j in range(n):
                if matrix[i][j]==1:
                    cnt+=1
            dgr.append(cnt)
        return dgr
# @lc code=end

