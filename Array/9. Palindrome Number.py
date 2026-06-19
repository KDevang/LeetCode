class Solution(object):
    def isPalindrome(self, x):
        x1= str(x)
        l= len(x1)
        a=""
        for i in range (l,0,-1):
            a+=(x1[i-1])
        if x1==a:
            return True
        else:
            return False
        