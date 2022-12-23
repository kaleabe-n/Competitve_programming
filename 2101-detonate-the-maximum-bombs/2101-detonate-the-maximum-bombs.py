class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        graph = defaultdict(lambda :[])
        for i in range(len(bombs)):
            for j in range(len(bombs)):
                bomb1 = bombs[i]
                bomb2 = bombs[j]
                dist = distance(bomb1[0],bomb1[1],bomb2[0],bomb2[1])
                if dist <= bomb1[2] and i!=j:
                    graph[i].append(j)
        maxDetonated = 0
        bombs = [i for i in range(len(bombs))]
        for j in bombs:
            stack = [j]
            visited = set([j])
            detonated = 1
            while stack:
                curr = stack.pop()
                for i in graph[curr]:
                    if i not in visited:
                        stack.append(i)
                        visited.add(i)
                        detonated+=1
            maxDetonated = max(maxDetonated,detonated)
        return maxDetonated
            

                
        
                
    
    
def distance(x1,y1,x2,y2):
    return sqrt((x2-x1)**2+(y2-y1)**2)
        