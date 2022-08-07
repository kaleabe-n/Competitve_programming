class Solution(object):
    def search(self, nums, target):
        left = 0
        right = len(nums)-1
        while left<right:
            if nums[left] <= nums[(right+left)//2] and nums[left] >= nums[0] and nums[(right+left)//2] > nums[right]:
                left = (right+left)//2+1
            else:
                right = (right+left)//2
        right = left+len(nums)-1
        while left<right:
            if nums[((left+right)//2)%len(nums)] >= target:
                right = (left+right)//2
            else:
                left = (left+right)//2+1
        return left%len(nums) if nums[left%len(nums)] == target else -1
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
