"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x:(x.start,-x.end))
        n = len(intervals)
        for i in range(n-1):
            if intervals[i+1].start<intervals[i].end:
                return False
        return True