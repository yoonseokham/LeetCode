class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        def lcm(a, b):
            def gcd(a, b):
                if b == 0:
                    return a
                return gcd(b, a % b)

            return a * b // gcd(a, b)

        return lcm(n, 2)
