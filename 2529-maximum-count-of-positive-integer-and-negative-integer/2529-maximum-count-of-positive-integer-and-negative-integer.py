class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        return max(len(nums) - self.getPostiveMin(nums),self.getNegativeMax(nums)+1)
    
    def getPostiveMin(self,nums):
        start = 0
        end = len(nums) - 1
        answer = len(nums)
        while start<=end:
            mid = (start+end)//2
            if nums[mid] <= 0:
                start = mid + 1
            elif nums[mid] > 0:
                answer = min(mid,answer)
                end = mid - 1
        return answer
    
    def getNegativeMax(self,nums):
        start = 0
        end = len(nums) - 1
        answer = -1
        while start<=end:
            mid = (start+end)//2
            if nums[mid] >= 0:
                end = mid - 1
            elif nums[mid] < 0:
                answer = max(mid,answer)
                start = mid + 1
        return answer