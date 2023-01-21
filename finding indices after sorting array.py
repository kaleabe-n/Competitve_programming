# class Solution(object):
#     def targetIndices(self, nums, target):
#         i = 0
#         while i < (len(nums) - 1):
#             if (nums[i] > nums[i + 1] and i >= 0):
#                 nums[i], nums[i + 1] = nums[i + 1], nums[i]
#                 i -= 1
#             else:
#                 i += 1
#         soln=[]
#         for i in range(len(nums)):
#             if nums[i]==target:
#                 soln.append(i)
#         return soln
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        lessThanCount = 0
        numCount = 0
        for num in nums:
            if num == target:
                numCount += 1
            elif num < target:
                lessThanCount += 1
        
        indices = []
        for i in range(numCount):
            indices.append(lessThanCount + i)
        
        return indices
