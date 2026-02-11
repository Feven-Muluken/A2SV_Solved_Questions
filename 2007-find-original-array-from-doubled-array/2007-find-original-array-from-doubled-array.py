
class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2 != 0:
            return []

        from collections import Counter
        changed.sort()
        count = Counter(changed)
        ans = []

        for x in changed:
            if count[x] == 0:
                continue

            if count[2 * x] == 0:
                return []

            ans.append(x)
            count[x] -= 1
            count[2 * x] -= 1

        return ans
