class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        n,m = len(matrix), len(matrix[0])
        dp=[[0 for i in range(m)] for j in range(n)]

        for i in range(m):
            dp[0][i] = matrix[0][i]
        for i in range(n):
            dp[i][0] = matrix[i][0]
        
        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][j] == 0:
                    dp[i][j] = 0
                else:
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
        s=0
        for i in range(n):
            s+=sum(dp[i])
        
        return s