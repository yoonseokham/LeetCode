import collections 
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if all(nums):
            return True
        visit = [False for _ in nums]
        visitable = set([0])
        queue = collections.deque([0])
        while queue:
            index = queue.popleft()
            visitable.discard(index)
            if index<len(visit):
                visit[index] = True
            if visit[-1]:
                return True
            for i in range(index+1,index+nums[index]+1):
                if i not in visitable:
                    visitable.add(i)
                    queue.append(i)
        return visit[-1]
            