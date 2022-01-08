class Solution(object):
    def rearrangeArray(self, nums):
        nums.sort()
        for i in range(0, len(nums) - 1, 2):
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
        return nums
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
