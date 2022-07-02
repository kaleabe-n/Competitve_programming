class Solution(object):
    def hasNoOverLap(self,li1,li2):
        if (li1[1]>=li2[0] and li1[0]<=li2[1]):
            return False
        return True
    def maxSumTwoNoOverlap(self, nums, firstLen, secondLen):
        prefixSum = [None]*len(nums)
        summ = 0
        firstSum = {}
        secondSum = {}
        for i in range(len(nums)):
            summ+=nums[i]
            prefixSum[i] = summ
        for i in range(len(nums)):
            if (i+firstLen-1)<len(nums):
                firstSum[(i,i+firstLen-1)] = prefixSum[i+firstLen-1]-prefixSum[i]+nums[i]
            if (i+secondLen-1)<len(nums):
                secondSum[(i,i+secondLen-1)] = prefixSum[i+secondLen-1]-prefixSum[i]+nums[i]
        maxSum = 0
        for i in firstSum:
            for j in secondSum:
                if self.hasNoOverLap(i,j):
                    maxSum = max(maxSum,firstSum[i]+secondSum[j])
        return maxSum
        """
        :type nums: List[int]
        :type firstLen: int
        :type secondLen: int
        :rtype: int
        """
        
