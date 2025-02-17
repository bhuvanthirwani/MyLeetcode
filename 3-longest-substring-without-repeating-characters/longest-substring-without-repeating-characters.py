class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=len(s)
        D=dict()
        i,j=0,0
        mv=0
        flag=0
        while(j<l):
            if(s[j] not in D):
                D[s[j]]=j
                mv=max(mv,j-i+1)
            else:
                t=D[s[j]]+1
                
                while(i!=t):
                    if(D[s[i]]<t):
                        D.pop(s[i])
                    else:
                        flag = 1
                        print("KFSFF",s[j], s[i], D[s[i]])
                    i+=1
                D[s[j]]=j
            #print(D)

            j+=1
            if flag == 1:
                return 0
        return mv