class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for s,e,t in times:
            graph[s].append([e,t])
            
        maxx = 0
        heap = [[0,k]]
        visited = set([k])
        while heap:
            dist,curr = heapq.heappop(heap)
            maxx = max(maxx,dist)
            for ne,w in graph[curr]:
                if ne not in visited:
                    heapq.heappush(heap,[w+dist,ne])
            visited.add(curr)
            if len(visited)==n:
                break
        return maxx if len(visited)==n else -1
