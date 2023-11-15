class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        counts = {}
        for num in arr:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
        
        occurrences = set()
        for k in counts:
            if counts[k] in occurrences:
                return False
            occurrences.add(counts[k])
        return True