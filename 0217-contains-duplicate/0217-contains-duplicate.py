class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num = dict()
        boolian = False
        for i in nums:
            if i not in num:
                num[i] = 1
            else:
                num[i] += 1
                if num[i] > 1:
                    boolian = True
        return boolian
            