class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        ns=set(nums)
        if len(ns)==len(nums):
            return False
        else:
            return True