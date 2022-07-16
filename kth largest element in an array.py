import heapq

class Solution(object):
    def findKthLargest(self, nums, k):
        heap = []
        for i in range(k):
            heapq.heappush(heap,nums[i])
        for i in range(k,len(nums)):
            if nums[i]>heap[0]:
                heapq.heappushpop(heap,nums[i])
        return heap[0]
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
