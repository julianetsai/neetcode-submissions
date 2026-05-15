class Solution:
    def insert(
        self, intervals: List[List[int]], newintervals: List[int]
    ) -> List[List[int]]:
        result = []
        # index tracker
        i = 0
        size = len(intervals)

        newStart, newEnd = newintervals

        # add all intervals that are before newintervals
        while i < size and intervals[i][1] < newStart:
            result.append(intervals[i])
            i += 1

        # now merge new intervals with any overlaps
        while i < size and intervals[i][0] <= newEnd:
            newStart = min(intervals[i][0], newStart)
            newEnd = max(intervals[i][1], newEnd)
            i += 1

        result.append([newStart, newEnd])

        # right side
        while i < size:
            result.append(intervals[i])
            i += 1

        return result
