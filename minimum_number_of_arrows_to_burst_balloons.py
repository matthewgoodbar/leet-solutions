class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        points.sort(key=lambda x:x[1])
        overlap = None
        overlaps = []
        for interval in points:
            if not overlap:
                overlap = interval
            else:
                if interval[0] <= overlap[1]:
                    #current interval overlaps with overlap
                    #update overlap
                    overlap = [max(interval[0],overlap[0]),min(interval[1],overlap[1])]
                else:
                    #current interval has no overlap with overlap
                    #add overlap to array, current interval starts new overlap
                    overlaps.append(overlap)
                    overlap = interval
        if overlap and overlaps[-1] != overlap:
            overlaps.append(overlap)
        return len(overlaps)

sol = Solution()
points = [[1,2],[3,4],[5,6],[7,8]]
print(sol.findMinArrowShots(points))