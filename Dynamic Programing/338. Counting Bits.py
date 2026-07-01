class Solution:
    def countBits(self, n: int) -> List[int]:
        l=[]
        for i in range(n+1):
            a=bin(i)
            l.append(a.count("1"))
        return(l)