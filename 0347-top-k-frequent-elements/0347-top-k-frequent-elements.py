class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        count = Counter(nums).most_common()
        num = []
        for x, i in count:
            if len(num) < k:
                num.append(x)
            else:
                break
        return num