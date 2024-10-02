class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n=len(temperatures)
        stack=[n-1]
        ans = [-1]*n
        ans[-1] = 0
        for i in range(n-2,-1,-1):
            while(len(stack) and temperatures[i] >= temperatures[stack[-1]]):
                stack.pop()
            if len(stack) == 0:
                ans[i] = 0
            else:
                ans[i] = stack[-1] - i
            stack.append(i)
        return ans
