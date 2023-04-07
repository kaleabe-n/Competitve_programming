class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for start,end in edges:
            graph[end].append(start)
        nonVisited = set(range(n))
        ans = set()
        while nonVisited:
            root = nonVisited.pop()
            stack = [root]
            while stack:
                curr  = stack.pop()
                if len(graph[curr]) == 0:
                    ans.add(curr)
                for neighbour in graph[curr]:
                    if neighbour in nonVisited:
                        stack.append(neighbour)
                        nonVisited.remove(neighbour)

            
        return list(ans)
