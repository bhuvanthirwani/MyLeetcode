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

    def maxAbsoluteSum(self, nums: List[int]) -> int:
        ans = -9999999999999999
        max_normal = self.kadane_algorithm(nums)
        for index in range(len(nums)):
            nums[index] = -1*nums[index]
        
        return max(self.kadane_algorithm(nums), max_normal)