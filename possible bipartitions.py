class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        for hater,hated in dislikes:
            graph[hater].append(hated)
            graph[hated].append(hater)
        nonVisited = set(range(1,n+1))
        set1 = set()
        set2 = set()
        while nonVisited:
            root = nonVisited.pop()
            stack = [(root,True)]
            while stack:
                curr,state = stack.pop()
                if state:
                    set1.add(curr)
                else:
                    set2.add(curr)
                state = not state
                for h in graph[curr]:
                    if h in nonVisited:
                        stack.append([h,state])
                        nonVisited.remove(h)
                    else:
                        if not state and h in set1:
                            return False
                        elif state and h in set2:
                            return False
                        
        return True
                
                
                
