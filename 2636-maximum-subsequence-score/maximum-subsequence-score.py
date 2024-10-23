import heapq as hq
class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        A=[]
        n=len(nums1)
        for i in range(n):
            A.append((nums1[i], nums2[i]))
        A.sort(key=lambda x: x[1], reverse=True)
        print(A)
        heap = []
        heapq.heapify(heap)
        presum = 0
        ans = 0
        for i in range(n):
            presum += A[i][0]
            heapq.heappush(heap, A[i][0])
            if len(heap) == k:
                p = heapq.heappop(heap)
                ans=max(ans, presum*A[i][1])
                presum -= p
        return ans
                