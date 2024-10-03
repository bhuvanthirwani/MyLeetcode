class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first_ele=second_ele=float('inf')
        for i in nums:
            if i<=first_ele:
                first_ele=i
            elif i<=second_ele:
                second_ele=i
            else:
                return True
        return False