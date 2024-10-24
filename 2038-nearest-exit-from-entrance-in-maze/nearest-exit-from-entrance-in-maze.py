from collections import deque
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        visited = set()
        inf, m, n = 9999999999999999999999999, len(maze), len(maze[0])
        offsets = [(1,0), (0,1), (0,-1), (-1,0)]
        maze[entrance[0]][entrance[1]] = 0
        queue = deque([(entrance[0], entrance[1])])
        visited.add((entrance[0], entrance[1]))
        dist=0
        print("Hello")
        while queue:
            count = len(queue)
            print("count: ", count)
            while count:
                p = queue.popleft()
                i,j=p[0],p[1]
                maze[i][j] = dist
                count -= 1
                for x,y in offsets:
                    if (i+x, j+y) not in visited and i+x>=0 and i+x <= m-1 and j+y>=0 and j+y<=n-1 and maze[i+x][j+y] == '.':
                        queue.append((i+x, j+y))
                        visited.add((i+x, j+y))
            dist += 1
        ans = inf
        print("Hurrah")
        for i in range(m):
            for j in range(n):
                if (i==0 or i==m-1 or j==0 or j==n-1) and maze[i][j] != '+' and maze[i][j] != '.' and not (i == entrance[0] and j == entrance[1]):
                    ans=min(ans, maze[i][j])
        return ans if ans != inf else -1