class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        num = []
        for i in nums:
            for j in str(i):
                m = "".join(j.split())
                num.append(int(m))
        return num