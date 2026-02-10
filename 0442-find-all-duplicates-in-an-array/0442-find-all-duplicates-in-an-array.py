class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        answer = []
        for i in nums:
            if nums.count(i) > 1 and i not in answer:
                answer.append(i)
        return answer