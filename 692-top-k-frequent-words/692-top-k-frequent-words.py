import heapq
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = {}
        for i in words:
            if i in count:
                count[i]+=1
            else:
                count[i] = 1
        heap = []
        for i in count:
            heapq.heappush(heap,[-count[i],i])
        ans = []
        for i in range(k):
            ans.append(heapq.heappop(heap)[-1])
            
        return ans