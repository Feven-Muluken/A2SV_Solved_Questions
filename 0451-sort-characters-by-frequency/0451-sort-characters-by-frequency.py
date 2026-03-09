class Solution:
    def frequencySort(self, s: str) -> str:
        from collections import Counter
        
        # s = list(s)
        s_counter = Counter(s)
        sorted_s = sorted(s, key=lambda x: (-s_counter[x], x))
        return "".join(sorted_s)
        # s.sort()
        # s_counter = Counter(s)
        # for i in range(len(s)):
        #     for j in range(len(s)-1):
        #         if s_counter[s[j]] < s_counter[s[j+1]]:
        #             s[j], s[j+1] = s[j+1], s[j]
                    
                
        # return "".join(s)