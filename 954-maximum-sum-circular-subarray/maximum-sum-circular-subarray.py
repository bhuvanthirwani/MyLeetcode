class Solution:
    def kadane_algorithm(self, nums):
        s=0
        res=-9999999
        for item in nums:
            s+=item
            res=max(res, s)
            if s<0:
                s=0
        return res
    
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        ans = -9999999999999999
        max_normal = self.kadane_algorithm(nums)
        if max_normal<0:
            return max_normal
        s=0
        for index in range(len(nums)):
            s+=nums[index]
            nums[index] = -1*nums[index]
        
        max_circular_subarray_sum = s + self.kadane_algorithm(nums)
        return max(max_circular_subarray_sum, max_normal)