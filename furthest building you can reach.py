import heapq

class Solution(object):
    def furthestBuilding(self, heights, bricks, ladders):
        heap = []
        for i in range(len(heights)-1):
            climb = heights[i+1] - heights[i]
            if climb<=0:
                continue
            if bricks>=climb:
                bricks-=climb
                heapq.heappush(heap,-climb)
                continue
            if len(heap)>0 and ladders>0 and -heap[0]>=climb:
                b = heapq.heapreplace(heap,-climb)
                ladders-=1
                bricks+=(-b)
                bricks-=climb
                continue
            elif ladders>0:
                ladders-=1
                continue
            if ladders == 0:
                return i
        return len(heights)-1
        """
        :type heights: List[int]
        :type bricks: int
        :type ladders: int
        :rtype: int
        """
        
