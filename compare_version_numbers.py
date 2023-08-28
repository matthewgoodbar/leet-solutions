class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        
        revisions1 = [int(rev) for rev in version1.split('.')][::-1]
        revisions2 = [int(rev) for rev in version2.split('.')][::-1]
        
        while revisions1 and revisions2:
            rev1 = revisions1.pop()
            rev2 = revisions2.pop()
            if rev1 < rev2:
                return -1
            elif rev1 > rev2:
                return 1
        
        if revisions1:
            remainders = [rev for rev in revisions1 if rev != 0]
            if remainders:
                return 1
        elif revisions2:
            remainders = [rev for rev in revisions2 if rev != 0]
            if remainders:
                return -1
        return 0

sol = Solution()
v1 = '0.1'
v2 = '1.1'
print(sol.compareVersion(v1, v2))