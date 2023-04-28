# class Solution:
#     def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
#         visited = set([0])
#         stack = [0]
#         while stack:
#             temp = stack.pop()
#             for i in rooms[temp]:
#                 if i not in visited:
#                     stack.append(i)
#                     visited.add(i)
#         return len(visited) == len(rooms)
        
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        que = collections.deque([0])
        visited = set([0])
        while que:
            curr = que.popleft()
            for room in rooms[curr]:
                if room not in visited:
                    visited.add(room)
                    que.append(room)
                    
        if len(visited) == len(rooms):
            return True
        return False
