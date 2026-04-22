class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        res = []
        total = rows * cols
        res.append([rStart, cStart])
        
        directions = [(0,1), (1,0), (0,-1), (-1,0)] 
        steps = 1
        d = 0 
        
        while len(res) < total:
            for _ in range(2):
                dr, dc = directions[d]
                for _ in range(steps):
                    rStart += dr
                    cStart += dc
                    if 0 <= rStart < rows and 0 <= cStart < cols:
                        res.append([rStart, cStart])
                        if len(res) == total:
                            return res
                d = (d + 1) % 4
            steps += 1
        
        return res
