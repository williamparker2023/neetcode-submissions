"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        ans = 0
        intervals.sort(key=lambda x:(x.start,x.end))
        hp = []
        n = len(intervals)

        for i in range(n):
            if not hp:
                heapq.heappush(hp,intervals[i].end)
                continue
            if hp[0] <= intervals[i].start:
                emptyRoom = heapq.heappop(hp)

            heapq.heappush(hp,intervals[i].end)

        print(hp)
        return len(hp)                
