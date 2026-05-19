import heapq

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        if not intervals:
            return 0

        # sort by start time
        intervals.sort(key=lambda x: x.start)

        # min heap stores ending times
        heap = [intervals[0].end]

        for interval in intervals[1:]:

            # if earliest room is free, reuse it
            if interval.start >= heap[0]:
                heapq.heappop(heap)

            # occupy room
            heapq.heappush(heap, interval.end)

        return len(heap)