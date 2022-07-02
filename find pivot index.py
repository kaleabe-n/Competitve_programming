class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefixSum = [None]*len(nums)
        for i in range(len(nums)):
            prefixSum[i] = prefixSum[i-1]+nums[i] if i>0 else nums[i]
        prefixSum.append(0)
        for i in range(len(nums)):
            if prefixSum[i-1] == (prefixSum[-2]-nums[i])/2:
                return i
        return -1
