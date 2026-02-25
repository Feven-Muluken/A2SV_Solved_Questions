class Solution:
    def findValidPair(self, s: str) -> str:
        from collections import Counter
        count = Counter(s)
        for i in range(len(s) - 1):
            a, b = s[i], s[i+1]
            if int(s[i]) == int(s[i+1]):  
                continue               
            if count[s[i]] == int(s[i]) and count[s[i+1]] == int(s[i+1]):
                return f"{s[i]}{s[i+1]}"
        return ""