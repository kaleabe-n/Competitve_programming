class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        prev = None
        for i,h in enumerate(heights):
            if i == 0 or h<=prev:
                prev = h
                continue
            curr = h-prev
            if curr<=bricks:
                bricks-=curr
                heapq.heappush(heap,-curr)
            else:
                if ladders>0:
                    ladders-=1
                    if not heap:
                        prev = h
                        continue
                    maxx = heapq.heappop(heap)
                    if curr>-maxx:
                        heapq.heappush(heap,maxx)
                    else:
                        bricks+=-maxx-curr
                        heapq.heappush(heap,-curr)
                    
                else:
                    return i-1
            prev = h
        return len(heights)-1
                


# import heapq

# class Solution(object):
#     def furthestBuilding(self, heights, bricks, ladders):
#         heap = []
#         for i in range(len(heights)-1):
#             climb = heights[i+1] - heights[i]
#             if climb<=0:
#                 continue
#             if bricks>=climb:
#                 bricks-=climb
#                 heapq.heappush(heap,-climb)
#                 continue
#             if len(heap)>0 and ladders>0 and -heap[0]>=climb:
#                 b = heapq.heapreplace(heap,-climb)
#                 ladders-=1
#                 bricks+=(-b)
#                 bricks-=climb
#                 continue
#             elif ladders>0:
#                 ladders-=1
#                 continue
#             if ladders == 0:
#                 return i
#         return len(heights)-1
#         """
#         :type heights: List[int]
#         :type bricks: int
#         :type ladders: int
#         :rtype: int
#         """
        
