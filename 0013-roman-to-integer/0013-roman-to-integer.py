class Solution:
    def romanToInt(self, s: str) -> int:
        dicti = {
            "I": 1, 
            "V": 5,
            "X": 10, 
            "L": 50,
            "C": 100, 
            "D": 500, 
            "M": 1000
        }
        _sum = 0
        for i in range(len(s)):
            if i+1 < len(s) and dicti[s[i]] < dicti[s[i+1]]:
                _sum-=dicti[s[i]] 
            else:
                _sum += dicti[s[i]] 
        return _sum