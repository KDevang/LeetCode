class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        for ch in s:
            if ch in t:
                pos = t.index(ch)
                t = t[pos + 1:]
            else:
                return False
        return True