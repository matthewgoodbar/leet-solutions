# Given an array of integers arr and an integer k. Find the least number of unique integers after removing exactly k elements.

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counts = {}
        for num in arr:
            if num not in counts:
                counts[num] = 1
            else:
                counts[num] += 1
        countList = list(counts.values())
        countList.sort(reverse=True)
        while k > 0:
            k -= countList[-1]
            if k >= 0: countList.pop()
        return len(countList)