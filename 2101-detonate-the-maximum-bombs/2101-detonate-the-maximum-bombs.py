class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        for i,bomb in enumerate(bombs):
            x,y,r = bomb
            for j,newBomb in enumerate(bombs):
                x2,y2,r2 = newBomb
                if i == j:
                    continue
                
                if sqrt((x-x2)**2+(y-y2)**2)<=r:
                    graph[i].append(j)
        maxCount = 0
        for i in range(len(bombs)):
            stack = [i]
            visited = set([i])
            count = 0
            while stack:
                curr = stack.pop()
                count += 1
                for n in graph[curr]:
                    if n not in visited:
                        visited.add(n)
                        stack.append(n)
            
            maxCount = max(maxCount,count)
                
        return maxCount




# class Solution:
#     def maximumDetonation(self, bombs: List[List[int]]) -> int:
#         graph = defaultdict(lambda :[])
#         for i in range(len(bombs)):
#             for j in range(len(bombs)):
#                 bomb1 = bombs[i]
#                 bomb2 = bombs[j]
#                 dist = distance(bomb1[0],bomb1[1],bomb2[0],bomb2[1])
#                 if dist <= bomb1[2] and i!=j:
#                     graph[i].append(j)
#         maxDetonated = 0
#         bombs = [i for i in range(len(bombs))]
#         for j in bombs:
#             stack = [j]
#             visited = set([j])
#             detonated = 1
#             while stack:
#                 curr = stack.pop()
#                 for i in graph[curr]:
#                     if i not in visited:
#                         stack.append(i)
#                         visited.add(i)
#                         detonated+=1
#             maxDetonated = max(maxDetonated,detonated)
#         return maxDetonated
       
    
# def distance(x1,y1,x2,y2):
#     return sqrt((x2-x1)**2+(y2-y1)**2)
        
