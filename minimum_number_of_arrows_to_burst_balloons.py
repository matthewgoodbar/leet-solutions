class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        points.sort(key=lambda x:x[1])
        overlap = None
        count = 0
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
                    count += 1
                    overlap = interval
        return count+1

sol = Solution()
points = [[1,2],[3,4],[5,6],[7,8]]
print(sol.findMinArrowShots(points))