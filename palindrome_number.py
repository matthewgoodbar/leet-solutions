# Given an integer x, return true if x is a palindrome, 
# and false otherwise.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        if x < 10: return True
        reversedX, chompedX = 0, x
        while chompedX > 0:
            digit = chompedX % 10
            reversedX = (reversedX * 10) + digit
            chompedX //= 10
        return x == reversedX