import heapq

class Solution(object):
    def lastStoneWeight(self, stones):
        heapq.heapify(stones)
        while len(stones)>1:
            largest = heapq.nlargest(2,stones)
            stones.remove(largest[0])
            stones.remove(largest[1])
            new = abs(largest[0]-largest[1])
            stones.append(new)
            heapq.heapify(stones)
        return 0 if len(stones) == 0 else stones[0] 
        """
        :type stones: List[int]
        :rtype: int
        """
        
