class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        isLastZero = False
        zeroCountList = [0 for i in range(len(nums))]
        for index, num in enumerate(nums):
            if not num:
                if not isLastZero:
                    isLastZero=True
                    zeroCountList[index] = 1
                else:
                    zeroCountList[index] = zeroCountList[index-1] + 1
            else:
                isLastZero = False
        return sum(zeroCountList)