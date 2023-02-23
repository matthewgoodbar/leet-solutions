# A valid IP address consists of exactly four integers separated by single dots. 
# Each integer is between 0 and 255 (inclusive) and cannot have leading zeros.

#     For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses, but "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses.

# Given a string s containing only digits, return all possible valid IP addresses that can be formed by inserting dots into s. 
# You are not allowed to reorder or remove any digits in s. 
# You may return the valid IP addresses in any order.

class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:

        def validateIP(s: str) -> bool:
            nums = s.split(".")
            for num in nums:
                if not num: return False
                if len(num) > 1 and num[0] == "0": return False
                if int(num) < 0 or int(num) > 255: return False
            return True
        
        def buildSubIPs(s: str, dots: int) -> list[str]:
            if dots == 0: 
                return [s] if validateIP(s) else []
            res = []
            for dotIndex in range(1, len(s) + dots - 1):
                first = s[:dotIndex]
                if not validateIP(first): continue
                remainder = buildSubIPs(s[dotIndex:], dots - 1)
                res = res + [first + "." + rem for rem in remainder]
            return res
        
        return buildSubIPs(s, 3)