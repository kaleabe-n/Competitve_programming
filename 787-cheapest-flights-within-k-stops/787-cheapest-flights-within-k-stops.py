# import heapq

# class Solution:
#     def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
#         graph = collections.defaultdict(list)
#         for start,end,price in flights:
#             graph[start].append([end,price])
#         heap = [[0,0,src]]
#         stops = {}
#         while heap:
#             pricePrev,stop,curr = heapq.heappop(heap)
#             if curr == dst and stop-1 <= k:
#                 return pricePrev
#             stops[curr] = stop if curr not in stops else min(stops[curr],stop)
#             for end,price in graph[curr]:
#                 if end not in stops or stops[end] > stop+1:
#                     heapq.heappush(heap,[pricePrev+price,stop+1,end])
#         return -1



# class Solution:
#     def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
#         graph = collections.defaultdict(list)
#         for start,end,price in flights:
#             graph[start].append([end,price])
#         que = [[0,0,src]]
#         visited = set()
#         stops = {}
#         while que:
#             prevDist,currK,node = heapq.heappop(que)
#             if node == dst and currK<=k+1:
#                 return prevDist
#             stops[node] = currK if node not in stops else min(currK,stops[node])
#             visited.add(node)
#             for n,dist in graph[node]:
#                 if n not in stops or stops[n]>currK+1:
#                     heapq.heappush(que,[prevDist+dist,currK+1,n])
#         return -1



class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for start,end,price in flights:
            graph[start].append([end,price])
        prev = [float('inf')]*n
        curr = [float('inf')]*n
        prev[src] = 0
        curr[src] = 0
        for _ in range(k+1):
            for i in range(n):
                for ne,cost in graph[i]:
                    curr[ne] = min(curr[ne],prev[i]+cost)
            prev,curr = curr,prev
        return prev[dst] if prev[dst]!=float('inf') else -1
        
        
