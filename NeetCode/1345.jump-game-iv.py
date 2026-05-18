# @lc app=leetcode id=1345 lang=python3
#
# [1345] Jump Game IV
#

# @lc code=start
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        queue = deque()
        visited = set()
        visited.add(0)
        n = len(arr)
        steps = 0
        queue.append(0)
        hashmap = defaultdict(list)
        if n == 1:
            return 0
        if arr[0] == arr[-1] and n>1:
            return 1
        for i,num in enumerate(arr):
            hashmap[num].append(i)
        while queue:
                _n = len(queue)
                for _ in range(_n):
                    temp = queue.popleft()
                    if temp == n-1:
                        return steps
                    if temp-1>=0:
                        if temp-1 not in visited:
                            visited.add(temp-1)
                            queue.append(temp-1)
                    if temp+1<n:
                        if temp+1 not in visited:
                            visited.add(temp+1)
                            queue.append(temp+1)
                    for i in hashmap[arr[temp]]:
                        if i not in visited:
                            visited.add(i)
                            queue.append(i)
                    hashmap[arr[temp]].clear()
                steps += 1
                     


# @lc code=end

