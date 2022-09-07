class Solution:

    def largestNumber(self, nums: List[int]) -> str:
        str_nums = list(
            map(lambda str_x: (str_x * (100 // len(str_x) + 1))[:100],
                list(map(str, nums))))
        answer_list = sorted(list(zip(str_nums, nums)), reverse=True)

        return str(int(''.join(str(num) for _, num in answer_list)))