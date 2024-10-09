from collections import deque
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        visited = set()
        queue = deque()
        ans = 0
        D={}
        V={}
        for bus_index in range(len(routes)):
            for v in routes[bus_index]:
                if bus_index in D:
                    D[bus_index][v] = 1
                else:
                    D[bus_index] = {}
                    D[bus_index][v] = 1
                if v not in V:
                    V[v] = {}
                V[v][bus_index] = 1
        if source not in V:
            return -1
        def insert_buses(vertex):
            for bus_index in V[vertex]:
                if bus_index not in visited:
                    queue.append(bus_index)
                    visited.add(bus_index)
                    # break
        insert_buses(source)
        # print('queue', queue, visited)
        while queue:
            count = len(queue)
            while(count):
                bus_index = queue.popleft()
                
                for v in routes[bus_index]:
                    if v == target:
                        # print("bus_index: ", bus_index, ans)
                        return ans + 1
                    insert_buses(v)
                    # p
                    # print("queue, 1.2: ", queue)
                count -= 1
            if queue:
                ans += 1
            else:
                return -1
            # print('queue2', queue, visited)
        if ans == 0:
            return -1
        return ans
        
        