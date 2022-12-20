class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        elemInd = {}
        for i in range(len(nums)):
            if target-nums[i]  in elemInd:
                return [elemInd[target-nums[i]],i]
            else:
                elemInd[nums[i]] = i
        