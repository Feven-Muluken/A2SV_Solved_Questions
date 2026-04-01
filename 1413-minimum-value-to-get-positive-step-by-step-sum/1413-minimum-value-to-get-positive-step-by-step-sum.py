class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        startValue = 1
        sumnums = startValue + nums[0]
        if len(nums) == 1:
            if nums[0] < 1:
                return abs(nums[0]) + 1
            else:
                return 1
        i = 1
        while i < len(nums):
            print(sumnums)
            if sumnums < 1:
                i = 1
                startValue += 1
                sumnums = startValue + nums[0]
            else:

                sumnums += nums[i]
                if sumnums < 1:
                    i = 1
                print(sumnums)
                i += 1
                print(startValue)
        return startValue