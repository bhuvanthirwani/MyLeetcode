import math
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        ans = max(nums)
        low, high=1, ans
        while(low<=high):
            mid = (low+high)//2
            s=0
            for i in nums:
                s+=math.ceil(i/mid)
                if s>threshold:
                    break
            if s>threshold:
                low=mid+1
            else:
                ans=mid
                high=mid-1
        return ans
        