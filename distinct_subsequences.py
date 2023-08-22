class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        facts = {}

        def factorial(n):
            if n in facts:
                return facts[n]
            if n <= 1:
                return 1
            res = n * factorial(n-1)
            facts[n] = res
            return res

        def choose(n, k):
            if k > n:
                return 0
            return factorial(n) // (factorial(k) * factorial(n - k))

        def compress(s):
            runningCount = 0
            res = []
            for i in range(len(s)):
                if i != 0 and s[i] != s[i-1]:
                    res.append((s[i-1], runningCount))
                    runningCount = 0
                runningCount += 1
            res.append((s[-1], runningCount))
            return res

        def sanitize(compS, compT):
            lettersWeCareAbout = set()
            for i in range(len(compT)):
                currentT = compT[i]
                for j in range(len(compS)):
                    currentS = compS[j]
                    if currentT[0] == currentS[0]:
                        newCompS = compS[j:]
                        newHead = [letter for letter in compS[:j] if letter[0] in lettersWeCareAbout]
                        compS = newHead + newCompS
                        lettersWeCareAbout.add(currentT[0])
                        break

            lettersWeCareAbout = set()
            for i in range(len(compT)-1, -1, -1):
                currentT = compT[i]
                for j in range(len(compS)-1, -1, -1):
                    currentS = compS[j]
                    if currentS[0] == currentT[0]:
                        newCompS = compS[:j+1]
                        newTail = [letter for letter in compS[j+1:] if letter[0] in lettersWeCareAbout]
                        compS = newCompS + newTail
                        lettersWeCareAbout.add(currentT[0])
                        break
            return compS
        
        def furtherSanitize(compS, compT):
            lettersWeCareAbout = set()
            for letter in compT:
                lettersWeCareAbout.add(letter[0])
            return [letter for letter in compS if letter[0] in lettersWeCareAbout]
        
        def compNumDistinct(compS, compT):
            
            if len(compT) == 1:
                count = 0
                for letter in compS:
                    if letter[0] == compT[0][0]:
                        count += letter[1]
                return choose(count, compT[0][1])
            
            compS = furtherSanitize(compS, compT)

            currentT = compT[0]
            count = 0
            matchingGroups = [i for i, letter in enumerate(compS) if letter[0] == currentT[0]]
            for i in range(len(matchingGroups)-1, -1, -1):
                currentS = compS[matchingGroups[i]]
                groupCounts = [letter[1] for letter in [compS[groupI] for groupI in matchingGroups[:i]]]
                prevChoice = None
                if groupCounts:
                    prevChoice = choose(sum(groupCounts), currentT[1])
                groupCounts.append(currentS[1])
                allChoice = choose(sum(groupCounts), currentT[1])
                if prevChoice and prevChoice > 0:
                    count += (allChoice - prevChoice) * compNumDistinct(compS[matchingGroups[i]+1:], compT[1:])
                else:
                    count += allChoice * compNumDistinct(compS[matchingGroups[i]+1:], compT[1:])
            
            return count
        
        compressedS = compress(s)
        compressedT = compress(t)
        compressedS = sanitize(compressedS, compressedT)
        print(len(compressedS))
        print(len(compressedT))
        return compNumDistinct(compressedS, compressedT)

s = "xslledayhxhadmctrliaxqpokyezcfhzaskeykchkmhpyjipxtsuljkwkovmvelvwxzwieeuqnjozrfwmzsylcwvsthnxujvrkszqwtglewkycikdaiocglwzukwovsghkhyidevhbgffoqkpabthmqihcfxxzdejletqjoxmwftlxfcxgxgvpperwbqvhxgsbbkmphyomtbjzdjhcrcsggleiczpbfjcgtpycpmrjnckslrwduqlccqmgrdhxolfjafmsrfdghnatexyanldrdpxvvgujsztuffoymrfteholgonuaqndinadtumnuhkboyzaqguwqijwxxszngextfcozpetyownmyneehdwqmtpjloztswmzzdzqhuoxrblppqvyvsqhnhryvqsqogpnlqfulurexdtovqpqkfxxnqykgscxaskmksivoazlducanrqxynxlgvwonalpsyddqmaemcrrwvrjmjjnygyebwtqxehrclwsxzylbqexnxjcgspeynlbmetlkacnnbhmaizbadynajpibepbuacggxrqavfnwpcwxbzxfymhjcslghmajrirqzjqxpgtgisfjreqrqabssobbadmtmdknmakdigjqyqcruujlwmfoagrckdwyiglviyyrekjealvvigiesnvuumxgsveadrxlpwetioxibtdjblowblqvzpbrmhupyrdophjxvhgzclidzybajuxllacyhyphssvhcffxonysahvzhzbttyeeyiefhunbokiqrpqfcoxdxvefugapeevdoakxwzykmhbdytjbhigffkmbqmqxsoaiomgmmgwapzdosorcxxhejvgajyzdmzlcntqbapbpofdjtulstuzdrffafedufqwsknumcxbschdybosxkrabyfdejgyozwillcxpcaiehlelczioskqtptzaczobvyojdlyflilvwqgyrqmjaeepydrcchfyftjighntqzoo"
t = "rwmimatmhydhbujebqehjprrwfkoebcxxqfktayaaeheys"
# s = "ababaaaaacccdddaaddbbbbaaaacccccddddaaaabbbb"
# t = "aabbbccccdd"
sol = Solution()
print(sol.numDistinct(s, t))