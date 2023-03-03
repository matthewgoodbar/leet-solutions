# Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.

# Since the result may be very large, so you need to return a string instead of an integer.

from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums: list[int]) -> str:

        def comparator(a, b):
            aOrder = int(str(a) + str(b))
            bOrder = int(str(b) + str(a))
            if aOrder > bOrder:
                return 1
            elif aOrder < bOrder:
                return -1
            else:
                return 0
        
        res = sorted(nums, key=cmp_to_key(comparator), reverse=True)
        res = ''.join([str(i) for i in res])
        return '0' if res[0] is '0' else res