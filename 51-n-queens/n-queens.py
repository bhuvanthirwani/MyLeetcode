class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        A = [['.' for i in range(n)] for j in range(n)]
        def isvalid(A, x, y):
            for i in range(n):
                if i!=x and A[i][y] == 'Q':
                    return False
            for j in range(n):
                if j!=y and A[x][j] == 'Q':
                    return False
            B= [(-1,-1), (1,1), (1,-1), (-1,1)]
            for p,q in B:
                a,b = x+p,y+q
                while(a<n and b<n and a>=0 and b>=0):
                    if A[a][b] == 'Q':
                        return False
                    a,b=a+p,b+q
            return True
        ans = []
        def fun(A, i):
            if i>=n:
                ans.append(["".join(A[l]) for l in range(n)])
            for x in range(n):
                if(isvalid(A, i, x)):
                    A[i][x] = 'Q'
                    fun(A, i+1)
                    A[i][x] = '.'
            return A
        fun(A, 0)
        return ans     