class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        for j in range(left, right+1):
            is_covered=False
            for i in ranges:
                if j in range(i[0], i[1]+1):
                    is_covered=True
                    break
            if not is_covered: return False
        return True
