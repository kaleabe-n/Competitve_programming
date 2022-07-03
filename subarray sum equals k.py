class Solution(object):
    def subarraySum(self, nums, k):
        prefixSumCount = {0:1}
        prefixSum = 0
        count = 0
        for i in nums:
            prefixSum+=i
            try:
                count+=prefixSumCount[prefixSum-k]
            except:
                pass
            if prefixSum in prefixSumCount:
                prefixSumCount[prefixSum]+=1
            else:
                prefixSumCount[prefixSum] = 1
        return count
            
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
