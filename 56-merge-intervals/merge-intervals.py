class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        start, end = intervals[0][0], intervals[0][1]
        intervals.sort(key=lambda x: x[0])
        ans = [intervals[0]]
        for a,b in intervals:
            if a<=ans[-1][1]:
                ans[-1][1]=max(ans[-1][1], b)
            else:
                ans.append([a,b])
        return ans