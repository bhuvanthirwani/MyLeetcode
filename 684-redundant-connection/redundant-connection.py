class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = {}
        for i,j in edges:
            if i not in graph:
                graph[i] = set()
            if j not in graph:
                graph[j] = set()
            graph[i].add(j)
            graph[j].add(i)
        visited = set()
        cycle_vertex = None
        def dfs(s, p):
            nonlocal cycle_vertex
            visited.add(s)
            print("s, p", s, p)
            for u in graph[s]:
                if u in visited and u!=p:
                    cycle_vertex = u
                if u not in visited:
                    dfs(u, s)
            return
        dfs(edges[0][0], -1)
        print('cycle_vertex', cycle_vertex)
        if cycle_vertex == None:
            return edges[-1]
        else:
            visited = set()
            stack, cyclic_vertices_list = [], []
            def find_cycle_vertices(s, p):
                nonlocal cycle_vertex, stack, cyclic_vertices_list
                visited.add(s)
                stack.append(s)
                # print("s: ", s, stack)
                for u in graph[s]:
                    # print("s: ", s, "neighbour: ", u)
                    if u==cycle_vertex:
                        print("return: ", stack)
                        if u!=p:
                            cyclic_vertices_list = stack[:]

                    if u not in visited:
                        find_cycle_vertices(u, s)
                stack.pop()
                return 
                
            find_cycle_vertices(cycle_vertex, -1)
            # print("cyclic vertices:", cyclic_vertices_list)
            ans=None
            for edge in edges:
                if edge[0] in cyclic_vertices_list and edge[1] in cyclic_vertices_list:
                    ans = edge
            return ans
            