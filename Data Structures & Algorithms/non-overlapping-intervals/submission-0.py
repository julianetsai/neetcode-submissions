class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # sort by start time.
        intervals.sort(key=lambda x: x[0])
        # keep a results array
        prevEnd = intervals[0][1]
        erase = 0
        # loop start , end of intervals:
        for start, end in intervals[1:]:
            # or no overlap
            if start >= prevEnd:
                prevEnd = end
            # overlap
            else:
                # if start < prev end , ++ and  keep min interval end time
                erase += 1
                prevEnd = min(end, prevEnd)

        return erase
