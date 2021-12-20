class Solution(object):
    def sortColors(self, nums):
        i=0
        while i < (len(nums)-1):
            if (nums[i] > nums[i + 1] and i>=0):
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                i-=1
            else:
                i += 1
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
