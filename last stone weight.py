class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        heapq.heapify(stones)
        while len(stones)>1:
            stone1 = heapq.heappop(stones)
            stone2 = heapq.heappop(stones)
            if stone1 != stone2:
                new = -abs(stone1-stone2)
                heapq.heappush(stones,new)
                
                
        return -stones[0] if stones else 0
                


# import heapq

# class Solution(object):
#     def lastStoneWeight(self, stones):
#         heapq.heapify(stones)
#         while len(stones)>1:
#             largest = heapq.nlargest(2,stones)
#             stones.remove(largest[0])
#             stones.remove(largest[1])
#             new = abs(largest[0]-largest[1])
#             stones.append(new)
#             heapq.heapify(stones)
#         return 0 if len(stones) == 0 else stones[0] 
#         """
#         :type stones: List[int]
#         :rtype: int
#         """
        
