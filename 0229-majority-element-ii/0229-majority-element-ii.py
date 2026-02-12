class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        from collections import Counter
        ans = []
        n = len(nums)/3
        num = Counter(nums)
        for element, count in num.items():
            if count > n:
                ans.append(element)
            else:
                continue
        return ans