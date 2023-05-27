class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        answer = 0
        nums.sort()
        for index in range(0,len(nums),2):
            answer += min(nums[index],nums[index+1])
        return answer