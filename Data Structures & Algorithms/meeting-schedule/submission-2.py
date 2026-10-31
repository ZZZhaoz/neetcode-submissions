"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        intervals.sort(key=lambda i: i.end)
        lastEnd = intervals[0].end
        res = 0

        for interval in intervals[1:]:
            
            if interval.start < lastEnd:
                res += 1
            else:
                lastEnd = interval.end
        return res == 0
