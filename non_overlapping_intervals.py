class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        # Sort by interval ends
        intervals.sort(key=lambda x: x[1])
        prevEnd = intervals[0][1]
        count = 0
        for i in range(1,len(intervals)):
            if prevEnd > intervals[i][0]:
                # If the previous interval end is strictly greater than
                # the current interval start, they overlap.
                # We can safely "discard" the current interval by
                # not reassigning prevEnd, increment count to
                # indicate deleted interval.
                count += 1
            else:
                # Current and previous intervals don't overlap, so we
                # can safely reassign prevEnd to current interval's end.
                prevEnd = intervals[i][1]
        return count

sol = Solution()
intervals = [[1,2],[2,3],[3,4],[1,3]]
print(sol.eraseOverlapIntervals(intervals))