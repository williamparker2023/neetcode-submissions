class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:(x[1]))
        i = 0
        ans = 0
        while i<len(intervals)-1:
            print(intervals)
            if intervals[i][1]>intervals[i+1][0]:
                ans+=1
                intervals = intervals[:i+1] + intervals[i+2:]
                i-=1
            i+=1
        return ans