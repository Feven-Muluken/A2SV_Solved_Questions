class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        # [1][1], ([1][2], [2][1]),  ([3][1], [2][2], [1][3]), ([2][3], [3][2]), [3][3]

        n = len(mat)
        m = len(mat[0])
        answer = []
        row, col = 0, 0
        up = True
        i = 0
        while i < (n*m):
            answer.append(mat[row][col])
            if up:
                if col == m-1:
                    row += 1
                    up = False
                elif row == 0:
                    col += 1
                    up = False
                else:
                    row -= 1
                    col += 1
            else:
                if row == n-1:
                    col += 1
                    up = True
                elif col == 0:
                    row += 1
                    up = True
                else:
                    row += 1
                    col -= 1
            i += 1
        return answer

        # while i < n*m:
        #     answer.append(mat[row][col])
        #     if row >= n or col >= n:
        #         return 
        #     if row == 0:
        #         up = False
        #     if row == n-1:
        #         up = True
        #     if up:
        #         row -= 1
        #         col += 1
        #     else:
        #         # answer.append(mat[row][col])
        #         row += 1
        #         col -= 1
                
        #     i += 1

        # return answer