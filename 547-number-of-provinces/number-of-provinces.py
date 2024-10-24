class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        n=len(isConnected)
        def dfs(s):
            visited.add(s)
            for i in range(n):
                if i not in visited and isConnected[s][i] == 1:
                    dfs(i)
            return
        count = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                count += 1
        return count