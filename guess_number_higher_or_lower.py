# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:

        def guessInRange(lower, upper):
        
            mid = (lower + upper) // 2
            match guess(mid):
                case 0:
                    return mid
                case 1:
                    return guessInRange(mid+1,upper)
                case -1:
                    return guessInRange(lower,mid-1)
        
        return guessInRange(1, n)