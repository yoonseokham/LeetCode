class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        start = -1
        end = len(nums)
        for index, value in enumerate(nums):
            if value < 0: start = index
            else: break
        for index in range(len(nums) - 1,-1,-1):
            value = nums[index]
            if value > 0: end = index
            else: break
        return max(start+1, len(nums) - end)
        