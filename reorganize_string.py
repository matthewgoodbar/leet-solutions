class Solution:
    def reorganizeString(self, s: str) -> str:

        if len(s) < 2:
            return s

        counts = {}
        maxCount = 0
        for char in s:
            if char not in counts:
                counts[char] = 1
            else:
                counts[char] += 1
            if counts[char] > maxCount:
                maxCount = counts[char]
                
        if maxCount - (len(s) - maxCount) > 1:
            return ""
        
        chars = list(counts.items())
        chars = sorted(chars, key=lambda x: x[1], reverse=True)

        def build(s, pool):

            if len(pool) == 1:
                if s[-1] != pool[0][0]:
                    if pool[0][1] == 1:
                        s = s + pool[0][0]
                        return s
                    else:
                        return None
                else:
                    return None
            
            for i, char in enumerate(pool):
                if s == "":
                    newS = s + char[0]
                    if char[1] == 1:
                        newPool = [el for el in pool if char[0] != el[0]]
                    else:
                        newPool = [el for el in pool]
                        newPool[i] = (char[0], char[1]-1)
                    res = build(newS, newPool)
                    if res:
                        return res
                else:
                    if char[0] != s[-1]:
                        newS = s + char[0]
                        if char[1] == 1:
                            newPool = [el for el in pool if char[0] != el[0]]
                        else:
                            newPool = [el for el in pool]
                            newPool[i] = (char[0], char[1]-1)
                        res = build(newS, newPool)
                        if res:
                            return res
            return None
        
        return build("", chars)
                        
                    

sol = Solution()
s = "helloworld"
print(sol.reorganizeString(s))