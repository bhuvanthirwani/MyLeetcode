class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n=len(nums)
        def binary_search(l, r, n):
            nonlocal nums
            while(l<=r):
                mid = (l+r)//2
                if mid==n-1:
                    if nums[mid] < nums[mid-1]:
                        return mid-1
                    else:
                        return mid
                if mid==0:
                    if nums[mid] < nums[mid+1]:
                        return mid+1
                    else:
                        return mid
                if (nums[mid] > nums[mid-1]) and (nums[mid] > nums[mid+1]):
                    return mid
                
                if nums[mid] <= nums[mid+1]:
                    l=mid+1
                else:
                    r=mid-1
        return binary_search(0, n-1, n)