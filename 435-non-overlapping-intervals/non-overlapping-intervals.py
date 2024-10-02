class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key= lambda x: x[1])
        curr_interval = intervals[0]
        i=1
        non_overlapping_intervals_count = 1
        n=len(intervals)
        while(i<n):
            if intervals[i][0] >= curr_interval[1]:
                curr_interval = intervals[i]
                non_overlapping_intervals_count += 1
                print("i: ", i)
            i+=1
        return n-non_overlapping_intervals_count
