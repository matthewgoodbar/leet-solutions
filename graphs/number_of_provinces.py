class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:

        provinces = 0
        visited = set()

        def dfs(city, province):
            province.add(city)
            visited.add(city)
            connectedCities = isConnected[city]
            for j in range(len(connectedCities)):
                if j not in province and connectedCities[j] == 1:
                    dfs(j, province)
        
        for i in range(len(isConnected)):
            if i not in visited:
                province = set()
                dfs(i, province)
                provinces += 1
        
        return provinces