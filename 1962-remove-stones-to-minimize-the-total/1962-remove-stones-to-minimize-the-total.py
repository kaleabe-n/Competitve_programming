class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles = [-x for x in piles]
        heapq.heapify(piles)
        for _ in range(k):
            curr = heapq.heappop(piles)
            curr = -curr
            curr -= curr//2
            heapq.heappush(piles,-curr)
        
        return -sum(piles)

# class Solution:
#     def minStoneSum(self, piles: List[int], k: int) -> int:
#         for i in range(len(piles)):
#             piles[i] = -piles[i]
#         heapq.heapify(piles)
#         while k>0:
#             maxx = -heapq.heappop(piles)
#             maxx = ceil(maxx/2)
#             heapq.heappush(piles,-maxx)
#             k-=1
#         return -sum(piles)
        
