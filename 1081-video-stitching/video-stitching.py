class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        jumps = [0]*(time+1)
        for i in clips:
            if i[0] < time:
                jumps[i[0]] = max(jumps[i[0]], i[1])
        max_reach = 0
        reach = 0
        ans=0
        #print(jumps)
        for i in range(time):
            max_reach = min(max(max_reach, jumps[i]), time)
            if i==reach:
                ans += 1
                reach = max_reach
                if i==reach:
                    return -1
            #print(i,jumps[i], max_reach, reach, ans)
        return ans