class Solution:

    def minimumDeletions(self, nums: List[int]) -> int:
        length = len(nums)
        max_element = max(nums)
        min_element = min(nums)
        max_index = nums.index(max_element)
        min_index = nums.index(min_element)

        first_index = min_index if max_index > min_index else max_index
        second_index = max_index if max_index > min_index else min_index

        def get_cost(length, from_front=True):
            if from_front:
                return lambda index: index + 1
            return lambda index: length - index

        get_front_cost = get_cost(length)
        get_back_cost = get_cost(length, False)

        cost_front_back = get_front_cost(first_index) + get_back_cost(
            second_index)
        cost_front = get_front_cost(second_index)
        cost_back = get_back_cost(first_index)
        return min((cost_front_back, cost_front, cost_back))
