class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 == '' or str2 == '':
            return ''
        
        def divides(divisor, dividend):
            if divisor == '' or dividend == '':
                return False
            if len(dividend) % len(divisor) != 0:
                return False
            return divisor * (len(dividend) // len(divisor)) == dividend
        
        gcd = ''
        for i in range(min(len(str1), len(str2))):
            if str1[i] != str2[i]:
                return ''
            else:
                candidate = str1[:i+1]
                if divides(candidate, str1) and divides(candidate, str2):
                    gcd = candidate
        return gcd