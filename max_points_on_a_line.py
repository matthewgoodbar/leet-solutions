# Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, 
# return the maximum number of points that lie on the same straight line.

class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:
        if len(points) < 2:
            return 1
        
        coefficients = {}
        for i in range(1, len(points)):
            for j in range(0, i):
                xi, yi = points[i]
                xj, yj = points[j]
                rise = yi - yj
                run = xi - xj
                if run == 0:
                    slope = 'inf'
                    intercept = xi
                else:
                    slope = rise / run
                    intercept = yi - (slope * xi)
                if (slope, intercept) not in coefficients:
                    coefficients[(slope, intercept)] = set()
                coefficients[(slope, intercept)].add((xi, yi))
                coefficients[(slope, intercept)].add((xj, yj))
        
        return len(max([coefficients[i] for i in coefficients], key=len))