class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        D={}
        n=len(s)
        for i in range(n-1,-1,-1):
            if s[i] not in D:
                D[s[i]] = i
        i=0
        segment_len = 0
        ans=[]
        limit = 0
        while(i<n):
            segment_len += 1
            limit=max(limit, D[s[i]])
            if i==limit:
                ans.append(segment_len)
                segment_len=0
            i+=1
        return ans
                
                