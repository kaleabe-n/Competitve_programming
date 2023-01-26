# class Solution:
#     def maxOperations(self, nums, k):
#         count=0 
#         keys = set(nums)
#         nums = Counter(nums)
#         for i in keys:
#             if i*2 == k:
#                 count += nums[i]//2
#             elif k-i in nums:
#                 count += max(nums[i], nums[k-i])-abs(nums[i]-nums[k-i])
#                 nums.pop(i)
#         return count
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: int
#         """
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        right = len(nums)-1
        count = 0
        while left < right:
            if nums[left] + nums[right] == k:
                count += 1
                left += 1
                right -= 1
            elif nums[left] + nums[right] > k:
                right -= 1
            elif nums[left] + nums[right] < k:
                left += 1
        return count
                
        
