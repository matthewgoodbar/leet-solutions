class Solution:
    def hIndex(self, citations: list[int]) -> int:
        maxVal = 0
        h = 0
        for c in citations:
            if c > maxVal:
                maxVal = c
                h = 1
        counts = [(None,0) for i in range(maxVal+1)]
        for c in citations:
            counts[c] = (c, counts[c][1])
            for i in range(c+1):
                counts[i] = (counts[i][0], counts[i][1]+1)
        print(counts)

        existingCounts = [count for count in counts if count[0] is not None]
        return max([min(count) for count in existingCounts])


sol = Solution()
citations = [3,0,6,1,5]
# citations = [11,15]
print(sol.hIndex(citations))