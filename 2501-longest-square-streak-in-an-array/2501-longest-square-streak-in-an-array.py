class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        num_set = frozenset(nums)
        num_sorted = sorted(nums)
        visited = set()
        answer = 1
        for num in num_sorted:
            if num not in visited:
                visited.add(num)
                last_num = num
                length = 1
                while last_num**2 in num_set:
                    last_num = last_num**2
                    visited.add(last_num)
                    length += 1
                answer = max(answer, length)
        return -1 if answer == 1 else answer
