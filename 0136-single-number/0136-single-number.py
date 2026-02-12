class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        from collections import Counter 
        count = Counter(nums)
        for i in count:
            if count[i] != 1:
                continue 
            else:
                return i