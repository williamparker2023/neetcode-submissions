"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals = sorted(intervals, key=lambda x: (x.start))
        #track max and cur overlaps
        heap = []
        ans = 0

        for i in range(len(intervals)):
            while heap and heap[0]<=intervals[i].start:
                heapq.heappop(heap)
            heapq.heappush(heap, intervals[i].end)
            ans = max(ans, len(heap))
        
        return ans