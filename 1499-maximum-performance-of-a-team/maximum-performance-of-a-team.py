class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        A=[]
        n=len(speed)
        for i in range(n):
            A.append((speed[i], efficiency[i]))
        A.sort(key=lambda x: x[1], reverse=True)
        print(A)
        heap = []
        heapq.heapify(heap)
        presum = 0
        ans = 0
        m = 10**9 + 7
        for i in range(n):
            presum += A[i][0]
            heapq.heappush(heap, A[i][0])
            ans=max(ans, presum*A[i][1])
            if len(heap) == k:
                p = heapq.heappop(heap)
                ans=max(ans, presum*A[i][1])
                presum -= p
        return ans%m