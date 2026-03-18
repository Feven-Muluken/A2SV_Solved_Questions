class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for a in range(int(math.sqrt(c)) + 1):
            b = c - a**2
            if int(math.sqrt(b))**2 == b:
                return True
        return False
        # return any(((a**2 + b**2) == c) for a in range(int(math.sqrt(c)) + 1) for b in range(int(math.sqrt(c)) + 1))