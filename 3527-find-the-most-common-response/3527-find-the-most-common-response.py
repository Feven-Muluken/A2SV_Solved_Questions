class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        from collections import Counter
        freq = Counter()

        for i in responses:
            today = set(i)

            for j in today:
                freq[j] += 1
        result = ""
        count = 0
        
        for i, j in freq.items():
            if j > count or ( j == count and (result == "" or i < result )):
                count = j
                result = i
        return result