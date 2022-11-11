class Solution(object):
    def findMaxLength(self, nums):
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i] = -1
        prefixSumIndex = {nums[0]:0}
        prefixSum = nums[0]
        maxLen = 0
        for i in range(1,len(nums)):
            prefixSum+=nums[i]
            if prefixSum == 0:
                maxLen = i+1
                if prefixSum not in prefixSumIndex:
                    prefixSumIndex[prefixSum] = i
            elif prefixSum in prefixSumIndex:
                maxLen = max(maxLen,i-prefixSumIndex[prefixSum])
            else:
                prefixSumIndex[prefixSum] = i
        return maxLen
        """
        :type nums: List[int]
        :rtype: int
        """
        