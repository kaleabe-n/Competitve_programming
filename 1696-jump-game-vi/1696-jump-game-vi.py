import heapq

class Solution(object):
    def maxResult(self, nums, k):
        heap = [[-nums[-1],len(nums)-1]]
        dp = [None]*len(nums)
        dp[-1] = nums[-1]
        for i in range(len(nums)-2,-1,-1):
            if heap[0][1]>i+k:
                while heap[0][1]>i+k:
                    heapq.heappop(heap)
            dp[i] = -heap[0][0] + nums[i]
            heapq.heappush(heap,[-dp[i],i])
        return dp[0]
        
                
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
         
