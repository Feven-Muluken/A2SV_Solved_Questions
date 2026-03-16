class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        from collections import Counter
        n = len(nums)
        freq = Counter(nums)
        
        # Find global dominant element
        dom, total_count = max(freq.items(), key=lambda x: x[1])
        
        left_count = 0
        for i in range(n - 1):
            if nums[i] == dom:
                left_count += 1
            
            # left length = i+1, right length = n-(i+1)
            if left_count * 2 > (i + 1) and (total_count - left_count) * 2 > (n - i - 1):
                return i
        
        return -1
