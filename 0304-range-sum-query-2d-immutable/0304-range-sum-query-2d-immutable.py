class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.rowsum = []
        for row in matrix:
            prefix = [0]
            for val in row:
                prefix.append(prefix[-1] + val)
            self.rowsum.append(prefix)
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = 0
        for r in range(row1, row2 + 1):
            total += self.rowsum[r][col2 + 1] - self.rowsum[r][col1]
        return total
        
# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)