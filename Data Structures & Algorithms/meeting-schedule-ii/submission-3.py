"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x:(x.start,x.end))
        if len(intervals)==0:
            return 0
        hp = [intervals[0].end]
        n = len(intervals)
        ans = 1
        for i in range(1,n):
            if intervals[i].start < hp[0]:
                ans+=1
            else:
                heapq.heappop(hp)
            heapq.heappush(hp,intervals[i].end)
        return ans
