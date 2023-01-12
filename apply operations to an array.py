class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        #perform the operations
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
        
        #push the zeros to the right
        left = 0
        right = 0
        while right < len(nums):
            if nums[left] != 0:
                left += 1
            while right <= left:
                right += 1
            while right <  len(nums) and nums[right] == 0:
                right += 1
            if right < len(nums) and nums[left] == 0 and nums[right] != 0 and left != right:
                nums[left],nums[right] = nums[right],nums[left]
                left += 1
                right += 1
        return nums
