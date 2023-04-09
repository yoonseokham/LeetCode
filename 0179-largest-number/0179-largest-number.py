class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        answer = "".join(i for _,i in sorted(list((i*100,i) for i in map(str, nums)),reverse=True))
        if answer.startswith('0'):
            return '0'
        return answer