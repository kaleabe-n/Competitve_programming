class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        prefixSum = [nums[0]]
        for i in range(1,len(nums)):
            prefixSum.append(prefixSum[-1]+nums[i])
        minInd = None
        minVal = float('inf')
        for i in range(len(nums)):
            rightCount = len(nums)-i-1 if i!=len(nums)-1 else 1
            if abs(int(prefixSum[i]/(i+1))-int((prefixSum[-1]-prefixSum[i])/rightCount)) < minVal:
                minVal = abs(int(prefixSum[i]/(i+1))-int((prefixSum[-1]-prefixSum[i])/rightCount))
                minInd = i
        return minInd