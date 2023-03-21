# You have a long flowerbed in which some of the plots are planted, and some are not. 
# However, flowers cannot be planted in adjacent plots.

# Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, 
# return if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule.

class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        
        if n == 0:
            return True

        for idx, bed in enumerate(flowerbed):
            if bed == 0:
                if (idx == 0 or flowerbed[idx-1] == 0) and (idx == len(flowerbed) - 1 or flowerbed[idx+1] == 0):
                    flowerbed[idx] = 1
                    n -= 1
                    if n == 0:
                        return True
        
        return False