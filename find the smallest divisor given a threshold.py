import math

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l = 1
        r = max(nums)
        while l<=r:
            mid = (l+r)//2
            currSum = dividendSum(nums,mid)
            if currSum<=threshold:
                r=mid-1
            else:
                l=mid+1
        return r+1
            
            
def dividendSum(arr,num):
    summ = 0
    for n in arr:
        summ+=int(math.ceil(n/num))
    return summ
    




# import math

# class Solution(object):
#     def smallestDivisor(self, nums, threshold):
#         right = max(nums)
#         left = 1
#         while right>left:
#             summ = 0
#             mid = (left+right)//2
#             for i in nums:
#                 summ+=math.ceil(float(i)/mid)
#             if summ>threshold:
#                 left = (left+right)//2+1
#             else:
#                 right = (left+right)//2
#         return right
                
#         """
#         :type nums: List[int]
#         :type threshold: int
#         :rtype: int
#         """
        
