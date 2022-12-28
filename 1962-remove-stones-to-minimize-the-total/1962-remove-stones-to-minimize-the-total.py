class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        for i in range(len(piles)):
            piles[i] = -piles[i]
        heapq.heapify(piles)
        while k>0:
            maxx = -heapq.heappop(piles)
            maxx = ceil(maxx/2)
            heapq.heappush(piles,-maxx)
            k-=1
        return -sum(piles)
        