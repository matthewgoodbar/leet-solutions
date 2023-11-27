class Solution:
    def minReorder(self, n: int, connections: list[list[int]]) -> int:

        self.flips = 0
        inbound = {}
        outbound = {}

        for con in connections:
            source, dest = con
            if source in outbound:
                outbound[source].add(dest)
            else:
                outbound[source] = {dest}
            if dest in inbound:
                inbound[dest].add(source)
            else:
                inbound[dest] = {source}
        
        visited = set()
        def dfs(city):
            visited.add(city)
            if city in inbound:
                for inboundCity in inbound[city]:
                    if inboundCity not in visited:
                        dfs(inboundCity)
            if city in outbound:
                for outboundCity in outbound[city]:
                    if outboundCity not in visited:
                        self.flips += 1
                        dfs(outboundCity)
        
        dfs(0)
        return self.flips

sol = Solution()
connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
n = 6
print(sol.minReorder(n, connections))