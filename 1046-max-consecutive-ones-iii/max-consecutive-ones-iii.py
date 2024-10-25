class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        D={0:0, 1:0}
        i, j, n, ans = 0, 0, len(nums), 0
        while i<=j and j<n:
            D[nums[j]] += 1
            if D[0]<=k:
                ans=max(ans, D[0] + D[1])
            else:
                while(i<n and D[0] > k):
                    D[nums[i]]-=1
                    i+=1
                    ans=max(ans, D[0]+D[1])
            j+=1
        return ans
