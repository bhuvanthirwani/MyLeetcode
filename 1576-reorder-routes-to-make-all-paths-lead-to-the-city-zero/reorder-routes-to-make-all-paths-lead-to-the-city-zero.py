class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        directed_graph = {}
        undirected_graph = {}
        for connection in connections:
            if connection[0] not in directed_graph:
                directed_graph[connection[0]] = {}
            if connection[1] not in directed_graph:
                directed_graph[connection[1]] = {}
            directed_graph[connection[0]][connection[1]] = 1
            if connection[0] not in undirected_graph:
                undirected_graph[connection[0]] = {}
            if connection[1] not in undirected_graph:
                undirected_graph[connection[1]] = {} 
            undirected_graph[connection[0]][connection[1]] = 1
            undirected_graph[connection[1]][connection[0]] = 1
        
        visited = set()
        count = 0
        def dfs(s):
            nonlocal count
            visited.add(s)
            for u in undirected_graph[s]:
                if u not in visited:
                    if s not in directed_graph[u]:
                        count += 1
                    dfs(u)
            return
        dfs(0)
        return count
