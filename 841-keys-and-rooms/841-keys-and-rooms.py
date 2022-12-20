class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set([0])
        stack = [0]
        while stack:
            temp = stack.pop()
            for i in rooms[temp]:
                if i not in visited:
                    stack.append(i)
                    visited.add(i)
        return len(visited) == len(rooms)
        