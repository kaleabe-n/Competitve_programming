class Solution(object):
    def targetIndices(self, nums, target):
        i = 0
        while i < (len(nums) - 1):
            if (nums[i] > nums[i + 1] and i >= 0):
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                i -= 1
            else:
                i += 1
        soln=[]
        for i in range(len(nums)):
            if nums[i]==target:
                soln.append(i)
        return soln
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
