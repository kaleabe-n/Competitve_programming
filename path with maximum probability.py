class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = collections.defaultdict(list)
        for i in range(len(edges)):
            l,r = edges[i]
            graph[l].append([r,succProb[i]])
            graph[r].append([l,succProb[i]])
        que = [[-1,start_node]]
        visited = set()
        while que:
            currProb,currNode = heapq.heappop(que)
            if currNode == end_node:
                return -currProb
            visited.add(currNode)
            for ne,prob in graph[currNode]:
                if ne not in visited:
                    heapq.heappush(que,[currProb*prob,ne])
        return 0
