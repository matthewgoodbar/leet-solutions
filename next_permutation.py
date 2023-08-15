class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def inPlaceSort(start, end):
            alreadySorted = False
            while not alreadySorted:
                alreadySorted = True
                for i in range(start, end):
                    if nums[i] > nums[i+1]:
                        nums[i], nums[i+1] = nums[i+1], nums[i]
                        alreadySorted = False
        
        def isLexicographicallyMaximized(start):
            #Assuming all smaller subgroups are maximized
            return nums[start] >= nums[start+1]
        
        def nextPerm(start, end):
            lexicoNext = None
            for i in range(start+1, end+1):
                if nums[i] > nums[start]:
                    if not lexicoNext:
                        lexicoNext = i
                    else:
                        if nums[i] < nums[lexicoNext]:
                            lexicoNext = i
            nums[start], nums[lexicoNext] = nums[lexicoNext], nums[start]
            inPlaceSort(start+1, end)
        
        start = len(nums)-2
        end = len(nums)-1
        while start > -1:
            if isLexicographicallyMaximized(start):
                start -= 1
            else:
                nextPerm(start, end)
                return None
        inPlaceSort(0, end)
        return None