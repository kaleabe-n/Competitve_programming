class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            while i+1 != nums[i]:
                if nums[i]!=nums[nums[i]-1]:
                    nums[nums[i]-1],nums[i] = nums[i],nums[nums[i]-1]
                else:
                    break
                    
        for i,num in enumerate(nums):
            if i+1!=num:
                return [num,i+1]
