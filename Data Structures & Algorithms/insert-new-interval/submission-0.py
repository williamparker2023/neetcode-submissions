class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        startVal = newInterval[0]
        endVal = newInterval[1]
        for i in range(n):
            if intervals[i][0]<=newInterval[0] and intervals[i][1]>=newInterval[0]:
                startVal = min(startVal, intervals[i][0])
            if intervals[i][1]>=newInterval[1] and intervals[i][0]<=newInterval[1]:
                endVal = max(endVal,intervals[i][1])
        print(startVal,endVal)
        ans = []
        injected = False
        for i in range(n):
            if intervals[i][1]<startVal:
                ans.append(intervals[i])
            else:
                break
        ans.append([startVal,endVal])
        for i in range(n):
            if intervals[i][0]>endVal:
                ans.append(intervals[i])
            
        return ans