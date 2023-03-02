

class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:

        def mergeSort(nums: list[int], start: int, end: int) -> list[int]:
            if (end - start) <= 1: return nums
            mp = ((end - start) // 2) + start
            mergeSort(nums, start, mp)
            mergeSort(nums, mp, end)
            merge(nums, start, end)
            return nums
        
        def merge(arr: list[int], start: int, end: int) -> list[int]:
            temp = [arr[i] for i in range(start, end)]
            mp = len(temp) // 2
            leftIdx, rightIdx = 0, mp
            arrIdx = start
            while (leftIdx < mp) and (rightIdx < len(temp)):
                if temp[leftIdx] <= temp[rightIdx]:
                    arr[arrIdx] = temp[leftIdx]
                    leftIdx += 1
                else:
                    arr[arrIdx] = temp[rightIdx]
                    rightIdx += 1
                arrIdx += 1
            while leftIdx < mp:
                arr[arrIdx] = temp[leftIdx]
                leftIdx += 1
                arrIdx += 1
            while rightIdx < len(temp):
                arr[arrIdx] = temp[rightIdx]
                rightIdx += 1
                arrIdx += 1
            return arr
        
        mergeSort(nums, 0, len(nums))
        return nums


arr = [5,2,3,1]
sol = Solution()
sol.sortArray(arr)
print(arr)