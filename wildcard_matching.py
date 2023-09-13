class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        def chunkP(p):
            res = []
            current = ''
            for char in p:
                if char == '*':
                    if current != '':
                        res.append(current)
                        current = ''
                else:
                    current = current + char
            if current != '':
                res.append(current)
            return res
        
        def chunkMatch(sChunk, pChunk):
            if len(sChunk) != len(pChunk):
                return False
            for i in range(len(pChunk)):
                if pChunk[i] == '?':
                    continue
                else:
                    if pChunk[i] != sChunk[i]:
                        return False
            return True

        def matchRec(s, chunks):

            if len(chunks) == 0:
                return True if len(s) == 0 else False
            
            if len(chunks) == 1:
                return chunkMatch(s, chunks[0])

            pChunk = chunks[0]
            for i in range(len(s)-len(pChunk)):
                sChunk = s[i:i+len(pChunk)]
                if chunkMatch(sChunk, pChunk):
                    if matchRec(s[i+len(pChunk)], chunks[1:]):
                        return True
            return False
        
        chunkedP = chunkP(p)
        print(chunkedP)
        return matchRec(s, chunkedP)

sol = Solution()
s = 'aa'
p = '*'
print(sol.isMatch(s, p))