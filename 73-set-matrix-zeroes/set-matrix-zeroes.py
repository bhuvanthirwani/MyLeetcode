class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n,m = len(matrix), len(matrix[0])
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    for k in range(n):
                        if matrix[k][j] != 0:
                            matrix[k][j] = '.'
                    for k in range(m):
                        if matrix[i][k] != 0:
                            matrix[i][k] = '.'
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == '.':
                    matrix[i][j] = 0
        return matrix