class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        ans=0
        n=len(grid)
        for i in range(n):
            row=grid[i]
            same=True
            for j in range(n):
                column=[grid[k][j] for k in range(n)]
                if column==row:
                    ans+=1
        return ans
            