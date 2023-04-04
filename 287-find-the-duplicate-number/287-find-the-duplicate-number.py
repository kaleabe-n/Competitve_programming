class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            while nums[i]!=i+1:
                if nums[i]!=nums[nums[i]-1]:
                    nums[nums[i]-1],nums[i] = nums[i],nums[nums[i]-1]
                else:
                    break
            
        for i,num in enumerate(nums):
            if i+1!=num:
                return num

# class Solution:
#     def findDuplicate(self, nums: List[int]) -> int:
#         left = 1
#         right = len(nums)-1
#         while left<right:
#             count = 0
#             for i in nums:
#                 if i<=(right+left)//2:
#                     count+=1
#             if count<=(right+left)//2:
#                 left = (right+left)//2+1
#             else:
#                 right = (right+left)//2
#         return left
