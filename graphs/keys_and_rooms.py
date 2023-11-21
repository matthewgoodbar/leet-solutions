class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        
        visited = set()

        def dfs(room):
            visited.add(room)
            keys = rooms[room]
            for key in keys:
                if key not in visited:
                    dfs(key)
        
        dfs(0)
        return len(visited) == len(rooms)