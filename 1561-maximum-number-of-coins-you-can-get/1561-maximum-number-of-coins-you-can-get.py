class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        print(piles)
        n = len(piles)
        count = 0
        for i in range(1, n - (n//3), 2):
            count += piles[i]
        return count