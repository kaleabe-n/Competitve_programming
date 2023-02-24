class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        summ = 0
        minLen = float('inf')
        for right in range(len(nums)):
            summ+=nums[right]
            while summ>=target:
                minLen = min(minLen,right-left+1)
                summ -= nums[left]
                left+=1
        return minLen if minLen != float('inf') else 0

# class Solution(object):
#     def minSubArrayLen(self, target, nums):
#         prefixSum = [nums[0]]
#         for i in range(1,len(nums)):
#             prefixSum.append(prefixSum[-1]+nums[i])
#         prefixSum.append(0)
#         i = 0
#         j = 0
#         soln = float('inf')
#         while j<len(nums):
#             if prefixSum[j]-prefixSum[i-1]>=target:
#                 soln = min(j-i+1,soln)
#                 if  j>i:
#                     i+=1
#                 else:
#                     j+=1
#             else:
#                 j+=1
#         if soln == float('inf'):
#             return 0
#         return soln
#         """
#         :type target: int
#         :type nums: List[int]
#         :rtype: int
#         """
