"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        sorted_interval = sorted(intervals, key = lambda i : i.start)

        for i in range(len(intervals) - 1):
            i1 = sorted_interval[i]
            i2 = sorted_interval[i + 1]
            if i1.end > i2.start:
                return False

        return True