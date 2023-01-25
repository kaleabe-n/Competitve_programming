class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0
        right = 0
        prev = None
        while right<len(nums):
            if nums[right] != prev:
                prev = nums[right]
                nums[left],nums[right] = nums[right],nums[left]
                left += 1
            right += 1
        return left