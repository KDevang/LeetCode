class Solution(object):
    def romanToInt(self, s):
        f=0
        roman_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
            }
        for i in range(len(s)-1):
            if roman_dict[s[i]] < roman_dict[s[i+1]]: 
                f-= roman_dict[s[i]]
            else:
                f+= roman_dict[s[i]]
        f += roman_dict[s[-1]]
        return f