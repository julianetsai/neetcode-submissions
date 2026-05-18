class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = [] 
        intervals.sort(key=lambda x: x[0])
        for start,end in intervals:
            # no overlap, add curr interval
            if not result or start > result[-1][1]: 
                result.append([start,end])
            # overlap is if start < last end. then we want to merge to prevStart currEnd.  

            else:
                result[-1][1]= max(result[-1][1], end)

        return result


