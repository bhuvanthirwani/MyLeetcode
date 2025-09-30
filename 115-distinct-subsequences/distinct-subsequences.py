class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        count = 0
        n,m=len(s),len(t)
        dp={}
        def fun(i,j):
            if j==m:
                return 1
            if i==n:
                return 0
            if (i,j) in dp:
                return dp[(i,j)]
            if s[i]==t[j]:
                dp[(i,j)] = fun(i+1,j+1) + fun(i+1,j)
                return dp[(i,j)]
            dp[(i,j)] = fun(i+1,j)
            return dp[(i,j)]
        return fun(0,0)