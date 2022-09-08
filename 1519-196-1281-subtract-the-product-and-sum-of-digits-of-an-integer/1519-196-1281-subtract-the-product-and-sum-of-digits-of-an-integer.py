class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum = 0
        mul = 1
        for i in str(n):
            mul *= int(i)
            sum += int(i)
        return mul - sum