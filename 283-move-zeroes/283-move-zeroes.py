class Solution(object):
    def moveZeroes(self, nums):
        i = 0
        while i<len(nums):
            if nums[i] == 0:
                break
            i+=1
        if i == len(nums)-1:
            return
        j = i+1
        while j<len(nums):
            if nums[j] != 0:
                nums[j],nums[i] = nums[i],nums[j]
                i+=1
                j+=1
            else:
                j+=1
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        