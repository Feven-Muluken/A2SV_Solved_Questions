class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = dict()
        for i in nums:
            if i not in count:
                count[i] = 1
            else:
                count[i] += 1
        return [x for x in count if count[x] == 1][0]