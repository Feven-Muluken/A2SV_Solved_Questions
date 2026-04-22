class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)

        def rotate(mat):
            # transpose
            for i in range(n):
                for j in range(i + 1, n):
                    mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
            # reverse rows
            for i in range(n):
                mat[i].reverse()

        # check 0°
        if mat == target:
            return True

        # check 90°, 180°, 270°
        for _ in range(3):
            rotate(mat)
            if mat == target:
                return True

        return False