class Solution(object):
    def moveZeroes(self, nums):
        i = 0
        count = 0
        while i < len(nums):
            if nums[i] == 0:
                nums.pop(i)
                count+=1
                i-=1
            i+=1
        for i in range(count):
            nums.append(0)
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
