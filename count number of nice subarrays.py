class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        oddCount = 0
        left = 0
        subarrays = 0
        odds = collections.deque()
        for right in range(len(nums)):
            if nums[right]%2 == 1:
                oddCount += 1
                odds.append(right)
            while oddCount > k:
                if nums[left]%2==1:
                    oddCount-=1
                if odds[0] == left:
                    odds.popleft()
                left += 1
            if len(odds) and oddCount == k:
                subarrays += odds[0] - left + 1
            
        return subarrays

# class Solution(object):
#     def numberOfSubarrays(self, nums, k):
#         oddPrefix = [None]*len(nums)
#         oddCount = 0
#         for i in range(len(nums)):
#             if nums[i]%2==1:
#                 oddCount+=1
#             oddPrefix[i]=oddCount
#         i = 0
#         j = 0
#         oddCount = 0
#         subarrayCount = 0
#         while True:
#             if i == 0:
#                 oddCount = oddPrefix[j]
#             else:
#                 oddCount = oddPrefix[j]-oddPrefix[i-1]
#             if (j==len(oddPrefix)-1 and oddCount<k)  or i>j:
#                 break
#             if oddCount<k:
#                 j+=1
#             elif oddCount == k and j<len(nums)-1:
#                 tempOddCount = oddCount
#                 temp = i
#                 while tempOddCount == k:
#                     subarrayCount+=1
#                     temp+=1
#                     tempOddCount=oddPrefix[j] if temp==0 else oddPrefix[j]-oddPrefix[temp-1]
#                 j+=1
#             elif oddCount == k and j==len(nums)-1:
#                 subarrayCount+=1
#                 i+=1
#             elif oddCount>k:
#                 i+=1
#             if j>=len(nums):
#                 j = len(nums)-1
#         return subarrayCount
            
                
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: int
#         """
