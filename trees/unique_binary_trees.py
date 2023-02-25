
class Solution:
    def numTrees(self, n: int) -> int:

        table = {}

        def numTreesWithRoot(root: int, bounds: list[int]):
            if len(bounds) == 1: return 1
            rootIdx = bounds.index(root)
            left = bounds[:rootIdx]
            right = bounds[rootIdx+1:]

            if len(left) not in table:
                numLeftTrees = sum([numTreesWithRoot(leftRoot, left) for leftRoot in left])
                if not numLeftTrees: numLeftTrees = 1
                table[len(left)] = numLeftTrees
            else:
                numLeftTrees = table[len(left)]
            
            if len(right) not in table:
                numRightTrees = sum([numTreesWithRoot(rightRoot, right) for rightRoot in right])
                if not numRightTrees: numRightTrees = 1
                table[len(right)] = numRightTrees
            else:
                numRightTrees = table[len(right)]
            
            return numLeftTrees * numRightTrees
        
        rangeList = list(range(1, n+1))
        return sum([numTreesWithRoot(root, rangeList) for root in rangeList])

sol = Solution()
print(sol.numTrees(19))