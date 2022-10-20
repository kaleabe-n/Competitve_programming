class Solution(object):
    def minSubArrayLen(self, target, nums):
        prefixSum = [nums[0]]
        for i in range(1,len(nums)):
            prefixSum.append(prefixSum[-1]+nums[i])
        prefixSum.append(0)
        i = 0
        j = 0
        soln = float('inf')
        while j<len(nums):
            if prefixSum[j]-prefixSum[i-1]>=target:
                soln = min(j-i+1,soln)
                if  j>i:
                    i+=1
                else:
                    j+=1
            else:
                j+=1
        if soln == float('inf'):
            return 0
        return soln
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """