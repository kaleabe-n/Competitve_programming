class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        prefixSum = [nums[0]]
        for i in range(1,len(nums)):
            prefixSum.append(prefixSum[-1]+nums[i])
        prefixSum.append(0)
        for i in range(len(nums)):
            leftSum = prefixSum[i-1]
            rightSum = prefixSum[-2]-prefixSum[i] 
            if leftSum == rightSum:
                return i
        return -1