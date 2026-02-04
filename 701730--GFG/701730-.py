class Solution:    
    def findUnion(self, a, b):
        # code here
        l = set(a + b)
        return list(l)