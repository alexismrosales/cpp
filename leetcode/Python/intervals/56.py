from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals
        intervals.sort(key=lambda x: x[0])
        mergedIntervals = [intervals[0]]
        i = 1
        while i < len(intervals):
            lastMerged = mergedIntervals[-1]
            # if mergedIntervals are overlapping
            if lastMerged[1] >= intervals[i][0]:
                mergedIntervals[-1][1] = max(lastMerged[1], intervals[i][1])
            else:
                mergedIntervals.append(intervals[i])
            i += 1
        return mergedIntervals
