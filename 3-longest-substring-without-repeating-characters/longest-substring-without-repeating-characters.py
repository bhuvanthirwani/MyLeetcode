class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=len(s)
        D=dict()
        i,j=0,0
        mv=0
        while(j<l):
            if(s[j] not in D):
                D[s[j]]=j
                mv=max(mv,j-i+1)
            else:
                t=D[s[j]]+1
                while(i!=t):
                    D.pop(s[i])
                    i+=1
                D[s[j]]=j
            j+=1
        return mv