class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSumCount = collections.defaultdict(int)
        prefixSumCount[0]=1
        prefix = 0
        subarrayCount = 0
        for num in nums:
            prefix+=num
            subarrayCount+=prefixSumCount[prefix-k]
            prefixSumCount[prefix]+=1
        return subarrayCount

# class Solution(object):
#     def subarraySum(self, nums, k):
#         prefixSumCount = {0:1}
#         prefixSum = 0
#         count = 0
#         for i in nums:
#             prefixSum+=i
#             try:
#                 count+=prefixSumCount[prefixSum-k]
#             except:
#                 pass
#             if prefixSum in prefixSumCount:
#                 prefixSumCount[prefixSum]+=1
#             else:
#                 prefixSumCount[prefixSum] = 1
#         return count
            
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: int
#         """
        
