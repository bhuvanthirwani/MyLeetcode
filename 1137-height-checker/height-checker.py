class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        H=heights[::]
        H.sort()
        ans=0
        for i in range(len(H)):
            if H[i] != heights[i]:
                ans += 1
        return ans