class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        D={0:0, 1:0}
        k=1
        i, j, n, ans = 0, 0, len(nums), 0
        while i<=j and j<n:
            D[nums[j]] += 1
            if D[0]<=k:
                if D[0] == 0:
                    ans=max(ans, D[1]-1)
                else:
                    ans=max(ans, D[1])
            else:
                while(i<n and D[0] > k):
                    D[nums[i]]-=1
                    i+=1
            j+=1
        return ans
                