class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sl=list(s)
        for i in t:
            if i in sl:
                sl.remove(i)
            else:
                return(i)