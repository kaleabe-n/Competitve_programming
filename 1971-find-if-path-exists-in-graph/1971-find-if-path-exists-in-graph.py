from collections import deque

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = {}
        for left,right in edges:
            if left in graph:
                graph[left].append(right)
            else:
                graph[left] = [right]
            if right in graph:
                graph[right].append(left)
            else:
                graph[right] = [left]
        que = deque([source])
        visited = set([source])
        while que:
            temp = que.popleft()
            if temp == destination:
                return True
            for i in graph[temp]:
                if i not in visited:
                    que.append(i)
                    visited.add(i)
        return False
        