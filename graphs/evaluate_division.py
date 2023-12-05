class Solution:
    def calcEquation(self, equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]:
        
        graph = {}

        def addEdge(a, b, val):
            if a in graph:
                graph[a].append((b, val))
            else:
                graph[a] = [(b,val)]
        
        for i in range(len(equations)):
            a, b = equations[i]
            val = values[i]
            addEdge(a,b,val)
            addEdge(b,a,1/val)
                        
        def dfs(node, target, visited):
            if node not in graph:
                return -1
            if node == target:
                return 1
            visited.add(node)
            for neighbor, val in graph[node]:
                if neighbor not in visited:
                    subRes = dfs(neighbor, target, visited)
                    if subRes != -1:
                        return subRes * val
            return -1
        
        res = []
        for query in queries:
            c, d = query
            subRes = dfs(c,d,set())
            if subRes != -1:
                addEdge(c,d,subRes)
                addEdge(d,c,1/subRes)
            res.append(subRes)
        return res


sol = Solution()
eqs = [["a","b"],["a","c"],["a","d"],["a","e"],["a","f"],["a","g"],["a","h"],["a","i"],["a","j"],["a","k"],["a","l"],["a","aa"],["a","aaa"],["a","aaaa"],["a","aaaaa"],["a","bb"],["a","bbb"],["a","ff"]]
vals = [1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0,11.0,1.0,1.0,1.0,1.0,1.0,3.0,5.0]
queries = [["d","f"],["e","g"],["e","k"],["h","a"],["aaa","k"],["aaa","i"],["aa","e"],["aaa","aa"],["aaa","ff"],["bbb","bb"],["bb","h"],["bb","i"],["bb","k"],["aaa","k"],["k","l"],["x","k"],["l","ll"]]
print(sol.calcEquation(eqs, vals, queries))