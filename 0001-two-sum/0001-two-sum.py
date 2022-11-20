import collections


class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        valueIndex = collections.defaultdict(list)
        
        for index, num in enumerate(nums):
            valueIndex[num].append(index)

        keySet = set(valueIndex.keys())
        for key in keySet:
            if target - key in keySet:
                if target - key == key and len(valueIndex[key]) >= 2:
                    return valueIndex[key]
                if target - key != key:
                    return [valueIndex[key][0], valueIndex[target - key][0]]
