#User function Template for python3

class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        # Your code here
        from collections import Counter
        a, b = Counter(a), Counter(b)
        return all(a[m] >= n for m, n in b.items())