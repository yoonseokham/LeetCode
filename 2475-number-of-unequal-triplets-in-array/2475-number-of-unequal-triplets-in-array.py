import collections
import functools
import itertools

class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        answer = 0
        index = [i for i in range(len(nums))]
        for i,j,k in itertools.combinations(index,3):
            if nums[i] != nums[j] and nums[j] != nums[k] and nums[i] != nums[k]:
                answer += 1
        return answer