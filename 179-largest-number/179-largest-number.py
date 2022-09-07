class Solution:

    def largestNumber(self, nums: List[int]) -> str:
        str_nums = list(
            map(lambda x: (str(x) * (100 // len(str(x)) + 1))[:100], nums))
        answer_list = sorted(list(zip(str_nums, nums)), reverse=True)

        return str(int(''.join(str(num) for _, num in answer_list)))