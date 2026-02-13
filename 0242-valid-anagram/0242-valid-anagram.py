class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # import itertools
        # sheffls = itertools.permutations(s)
        # sheffls = ["".join(i) for i in sheffls]
        # if t in sheffls:
        #     return True
        # return False
        if len(t) != len(s):
            return False
        return all(i in t and s.count(i) == t.count(i) for i in s)