class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        A=[]
        for i in nums:
            A.append(str(i))
        A.sort(key=lambda x: x*12, reverse=True)
        
        return ''.join(A) if A[0] != '0' else '0'