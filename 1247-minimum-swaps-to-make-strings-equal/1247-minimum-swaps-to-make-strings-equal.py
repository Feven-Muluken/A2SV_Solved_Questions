class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        xy = 0
        yx = 0
        
        # Count mismatches
        for a, b in zip(s1, s2):
            if a == 'x' and b == 'y':
                xy += 1
            elif a == 'y' and b == 'x':
                yx += 1
        
        # If odd total mismatches → impossible
        if (xy + yx) % 2 != 0:
            return -1
        
        # Each pair of xy mismatches needs 1 swap
        # Each pair of yx mismatches needs 1 swap
        # If one xy and one yx remain → 2 swaps
        return (xy // 2) + (yx // 2) + (2 if xy % 2 == 1 else 0)
