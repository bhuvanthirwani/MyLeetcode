class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        p,ans=0,-99999999
        for i in gain:
            p+=i
            ans=max(ans,p)
        return max(ans,0)