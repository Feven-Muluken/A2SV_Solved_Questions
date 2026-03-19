class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        from collections import defaultdict
        def atMostK(nums: List[int], K: int) -> int:
            count = defaultdict(int)
            left = 0
            res = 0
            distinct = 0

            for right, val in enumerate(nums):
                if count[val] == 0:
                    distinct += 1
                count[val] += 1

                while distinct > K:
                    count[nums[left]] -= 1
                    if count[nums[left]] == 0:
                        distinct -= 1
                    left += 1

                res += right - left + 1
            return res

        return atMostK(nums, k) - atMostK(nums, k - 1)
