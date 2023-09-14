class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:

        intervals.sort(key=lambda x: x[0])
        
        def mergePair(first, second):
            allTogether = first + second
            return [min(allTogether), max(allTogether)]
        
        allMerged = False
        while not allMerged:
            allMerged = True
            for i in range(len(intervals)-1):
                first = intervals[i]
                second = intervals[i+1]
                if second[0] in range(first[0],first[1]+1):
                    merged = mergePair(first, second)
                    intervals = intervals[:i] + [merged] + intervals[i+2:]
                    allMerged = False
                    break
        return intervals