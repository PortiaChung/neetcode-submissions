class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x)

        res = 0
        while x > 0:
            d = x % 10
            x = x // 10
            res = res * 10 + d
        res *= sign
        if -2**31 <= res <= 2**31-1:
            return res
        else:
            return 0
        