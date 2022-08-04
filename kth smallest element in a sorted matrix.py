import heapq

class Solution(object):
    def kthSmallest(self, matrix, k):
        heap = []
        for row in matrix:
            for element in row:
                if len(heap)<k:
                    heapq.heappush(heap,-element)
                elif -heap[0] > element:
                    heapq.heapreplace(heap,-element)
        return -heap[0]
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        
