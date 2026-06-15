class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        startIx = -1
        startVal = newInterval[0]
        ans = []
        i = 0
        n = len(intervals)
        while i<n and intervals[i][1]<newInterval[0]:
            ans.append(intervals[i])
            i+=1
            
        startIx = i
        if i<n:
            startVal = min(startVal,intervals[i][0])
        
        endVal = newInterval[1]
        while i<n and intervals[i][0]<=newInterval[1]:
            i+=1
            endVal = max(newInterval[1],intervals[max(0,i-1)][1])
        

        ans.append([startVal,endVal])

        while i<n:
            ans.append(intervals[i])
            i+=1

        return ans
