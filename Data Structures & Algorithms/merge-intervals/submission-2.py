class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        i = 0
        intervals.sort(key=lambda x:(x[0],x[1]))
        while i<len(intervals)-1:
            if intervals[i][1] >= intervals[i+1][0]:
                end = max(intervals[i][1],intervals[i+1][1])
                intervals = intervals[:i] + [[intervals[i][0],end]] + intervals[i+2:]
                i-=1
            i+=1
        return intervals