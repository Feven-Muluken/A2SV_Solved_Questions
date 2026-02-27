class Solution:
    def minSteps(self, s: str, t: str) -> int:
        from collections import Counter

        s_count = Counter(s)
        t_count = Counter(t)

        count = 0
        for i in s_count:
            if s_count[i] == t_count[i]:
                continue 
            if s_count[i] > t_count[i]:
                count += (t_count[i] - s_count[i])
            else:
                continue
        return abs(count)