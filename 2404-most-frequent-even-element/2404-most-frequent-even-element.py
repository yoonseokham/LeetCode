import collections


class Solution:

    def mostFrequentEven(self, nums: List[int]) -> int:
        data = collections.defaultdict(int)
        for num in nums:
            data[num] += 1
        result = sorted([i for i in data.keys() if not i % 2],
                        key=lambda x: (-data[x], x))
        return result[0] if result else -1
