class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        parents = [i for i in range(n)]
        for l,r in edges:
            lroot = root(l,parents)
            rroot = root(r,parents)
            parents[lroot] = parents[rroot]
        
        return root(source,parents) == root(destination,parents)
            
            
def root(node,parents):
    if node == parents[node]:
        return node
    currRoot = root(parents[node],parents)
    parents[node] = currRoot
    return currRoot



# from collections import deque

# class Solution:
#     def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
#         graph = {}
#         for left,right in edges:
#             if left in graph:
#                 graph[left].append(right)
#             else:
#                 graph[left] = [right]
#             if right in graph:
#                 graph[right].append(left)
#             else:
#                 graph[right] = [left]
#         que = [source]
#         visited = set([source])
#         while que:
#             temp = que.pop()
#             if temp == destination:
#                 return True
#             for i in graph[temp]:
#                 if i not in visited:
#                     que.append(i)
#                     visited.add(i)
#         return False
        
