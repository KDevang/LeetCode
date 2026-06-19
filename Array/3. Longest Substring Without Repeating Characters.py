class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        f=""
        ans=0
        for ch in s:
            if ch not in f:
                f+=ch
            else:
                while ch in f:
                    f = f[1:]
                f+=ch
            ans=max(ans,len(f))
        return ans