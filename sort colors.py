# class Solution(object):
#     def sortColors(self, nums):
#         i=0
#         while i < (len(nums)-1):
#             if (nums[i] > nums[i + 1] and i>=0):
#                 nums[i], nums[i + 1] = nums[i + 1], nums[i]
#                 i-=1
#             else:
#                 i += 1
#         """
#         :type nums: List[int]
#         :rtype: None Do not return anything, modify nums in-place instead.
#         """
        
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red = 0
        white = 0
        blue = 0
        for num in nums:
            if num == 0:
                red += 1
            elif num == 1:
                white += 1
            elif num == 2:
                blue += 1
        
        for i in range(len(nums)):
            if red > 0:
                red -= 1
                nums[i] = 0
            elif white > 0:
                white -= 1
                nums[i] = 1
            elif blue > 0:
                nums[i] = 2
                blue -= 1

