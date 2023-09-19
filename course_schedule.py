class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:

        def takeCourse(course):
            possible = True
            visited.add(course)
            for preReq in courseGraph[course]:
                if preReq in visited:
                    if preReq not in coursesTaken:
                        possible = False
                        break
                else:
                    possible = takeCourse(preReq)
                    if not possible:
                        break
            if possible:
                coursesTaken.add(course)
            return possible
        
        courseGraph = {}
        for i in range(numCourses):
            courseGraph[i] = []
        for preRequisite in prerequisites:
            course, preReq = preRequisite
            courseGraph[course].append(preReq)
        
        coursesTaken = set()
        visited = set()
        for i in range(numCourses):
            if not takeCourse(i):
                return False
        return len(coursesTaken) == numCourses