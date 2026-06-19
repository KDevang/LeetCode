class Solution:
    def reverse(self, x: int) -> int:
        xs=str(x)
        if "-" in xs:
            n=-int(xs[:0:-1])
        else:
            n=int(xs[::-1])
        if n < -2**31 or n > 2**31 - 1:
            return 0
        return n