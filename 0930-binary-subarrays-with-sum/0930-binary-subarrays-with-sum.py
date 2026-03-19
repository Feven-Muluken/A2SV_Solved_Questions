# class Solution:
#     def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
#         left = 0
#         right = len(nums)
#         count = 0
#         while left < right:
#             for i in range(len(nums)):
#                 if sum(nums[left: right]) == goal:
#                     count += 1
#                     continue
#                 elif sum(nums[left: right]) > goal:
#                     right -= 1
#             left += 1
#         return count


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix_sum = 0
        count = 0
        freq = defaultdict(int)
        freq[0] = 1

        for num in nums:
            prefix_sum += num
            count += freq[prefix_sum - goal]
            freq[prefix_sum] += 1

        return count