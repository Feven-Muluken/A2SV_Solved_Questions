class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        # for left in range(n-2):
        #     for mid in range(left+1, n-1):
        #         for right in range(mid+1,n):
        #             if nums[left] < nums[right] and nums[right] < nums[mid]:
        #                 return True
        # return False
        stack = []
        second = float('-inf')

        for i in range(n - 1, -1, -1):
            if nums[i] < second:
                return True

            while stack and nums[i] > stack[-1]:
                second = stack.pop()

            stack.append(nums[i])
        return False