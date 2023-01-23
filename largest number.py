# class Solution(object):
#     def largestNumber(self, nums):
#         st=""
#         for i in range(len(nums)):
#             nums[i]=str(nums[i])
#         while len(nums)>0:
#             large=nums[0]
#             index=0
#             for i in range(len(nums)):
#                 if (nums[i]+large)>(large+nums[i]):
#                     large=nums[i]
#                     index=i
#             st+=large
#             nums.pop(index)
#         if st[0]=='0':
#             return "0"
#         return st
#         """
#         :type nums: List[int]
#         :rtype: str
#         """
        
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for _ in range(len(nums)):
            for i in range(len(nums) - 1):
                len1 = len(str(nums[i]))
                len2 = len(str(nums[i+1]))
                num1 = nums[i] * (10 ** len2) + nums[i+1]
                num2 = nums[i+1] * (10 ** len1) + nums[i]
                if num2 > num1:
                    nums[i],nums[i+1] = nums[i+1],nums[i]
        for i in range(len(nums)):
            nums[i] = str(nums[i])
        ans = "".join(nums)
        return ans.lstrip("0") if len(ans.lstrip("0")) >= 1 else "0"
