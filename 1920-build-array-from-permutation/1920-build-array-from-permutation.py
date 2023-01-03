class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        length = len(nums)
        for i in range(length):
            ans = nums[nums[i]] % length
            nums[i] += ans * length
        for i in range(length):
            nums[i] //= length
            
        return nums