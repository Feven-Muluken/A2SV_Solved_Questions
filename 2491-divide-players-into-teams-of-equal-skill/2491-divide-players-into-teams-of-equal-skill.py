class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n = len(skill)
        if n%2 != 0:
            return -1
        skill.sort()
        target = skill[0] + skill[-1]
        n = len(skill)
        total = 0
        i, j = 0, n - 1
        while i < j:
            if skill[i] + skill[j] != target:
                return -1
            total += skill[i] * skill[j]
            i += 1
            j -= 1
        return total