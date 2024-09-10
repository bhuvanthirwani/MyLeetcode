class Solution:
    def find(self, x,y, A):
        count=0
        p,q=-1,-1
        for i in A:
            if p==-1 and x==i:
                p=count
            elif q==-1 and y==i:
                q=count
            count+=1
        return [p,q]
    def twoSum(self, A: List[int], target: int) -> List[int]:
        B=A[:]
        A.sort(reverse=True)
        i = 0
        j = len(A) - 1
        print(A)
        while i < j:
            if A[i] + A[j] == target:
                return self.find(A[i], A[j], B)
            elif A[i] + A[j] < target:
                j -= 1
            else:
                i += 1
        
        return []