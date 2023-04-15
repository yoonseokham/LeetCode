class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        isLastZero = False
        zeroCountList = [0 for i in range(len(nums))]
        answer = 0
        for index, num in enumerate(nums):
            if not num:
                if not isLastZero:
                    isLastZero=True
                    zeroCountList[index] = 1
                    answer += zeroCountList[index]
                else:
                    zeroCountList[index] = zeroCountList[index-1] + 1
                    answer += zeroCountList[index]
            else:
                isLastZero = False
        return answer