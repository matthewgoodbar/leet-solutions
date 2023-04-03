# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. 
# The digits are ordered from most significant to least significant in left-to-right order. 
# The large integer does not contain any leading 0's.

# Increment the large integer by one and return the resulting array of digits.

class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        pointer = len(digits) - 1
        carryOver = False
        while True:
            if pointer == -1:
                digits = [1] + digits
                break
            val = digits[pointer] + 1
            if val < 10:
                digits[pointer] = val
                carryOver = False
            else:
                digits[pointer] = 0
                pointer -= 1
                carryOver = True
            if not carryOver:
                break
        
        return digits