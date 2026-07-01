class Solution:
    def addDigits(self, num: int) -> int:
        n=list(str(num))
        while len(n)>1:
            n=list(str(sum(int(i) for i in n)))
        return int(n[0])