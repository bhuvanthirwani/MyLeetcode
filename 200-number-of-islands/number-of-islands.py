class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n,m=len(grid), len(grid[0])
        def fun(i,j):
            if i<0 or i==n or j==m or j<0 or grid[i][j] in ["0"]:
                return
            grid[i][j]="0"
            for a in [(1,0), (0,1), (-1, 0), (0,-1)]:
                fun(i+a[0], j+a[1])
            return 
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    # print(i,j)
                    fun(i,j)
                    count+=1
                    # print(grid)
        return count