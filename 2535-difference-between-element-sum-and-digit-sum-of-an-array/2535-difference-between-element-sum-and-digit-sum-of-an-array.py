class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        return abs(sum(nums) - sum(sum(int(i)for i in str(num)) for num in nums))