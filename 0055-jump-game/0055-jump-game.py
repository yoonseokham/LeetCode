import collections 
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if all(nums) or len(nums)==1:
            return True
        visitable = set([0])
        queue = collections.deque([0])
        while queue:
            index = queue.popleft()
            visitable.discard(index)
            for i in range(index+1,index+nums[index]+1):
                if i == len(nums)-1:
                    return True
                if i not in visitable and index<len(nums):
                    visitable.add(i)
                    queue.append(i)
        return False
            