class Solution:

    def largestNumber(self, nums: List[int]) -> str:
        str_nums = list(map(str, nums))
        str_nums = list(map(lambda x: (x * 100)[:100], str_nums))
        answer_list = sorted(list(zip(str_nums, nums)), reverse=True)

        return str(int(''.join(str(num) for _, num in answer_list)))