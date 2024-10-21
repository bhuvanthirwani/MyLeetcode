class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        def binary_search(jobs, low, high, current_job):
            ans = -1
            # print("################: ", low, high)
            while(low<=high):
                # print("low, high", low, high)
                mid=(low+high)//2
                if jobs[mid][0]<=current_job[1]:
                    ans = mid
                    low = mid+1
                else:
                    high = mid-1
            # print("Ans: ", ans)
            return ans
        jobs = []
        for i in range(len(profit)):
            jobs.append((endTime[i], startTime[i], profit[i]))
        jobs.sort()
        dp = [0]
        A=[]
        # print("Jobs: ", jobs)
        for i in range(0, len(jobs)):
            res = binary_search(jobs, 0, i-1, jobs[i])
            A.append(res)
        # print("A", A)
        for i in range(len(jobs)):
            
            if A[i] == -1:
                # print("i: ",i, max(dp[i-1], jobs[i][2]), dp[-1], jobs[i][2], dp)
                dp.append(max(dp[-1], jobs[i][2]))
            else:
                # print("i: ",i, max(dp[i-1], dp[A[i] + 1] + jobs[i][2]), dp[-1], dp[A[i] + 1] + jobs[i][2], dp)
                dp.append(max(dp[-1], dp[A[i] + 1] + jobs[i][2]))
        # print(A, dp)  
        return dp[-1]