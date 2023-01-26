import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for start,end,price in flights:
            graph[start].append([end,price])
        heap = [[0,0,src]]
        stops = {}
        while heap:
            pricePrev,stop,curr = heapq.heappop(heap)
            if curr == dst and stop-1 <= k:
                return pricePrev
            stops[curr] = stop if curr not in stops else min(stops[curr],stop)
            for end,price in graph[curr]:
                if end not in stops or stops[end] > stop+1:
                    heapq.heappush(heap,[pricePrev+price,stop+1,end])
        return -1
        
        