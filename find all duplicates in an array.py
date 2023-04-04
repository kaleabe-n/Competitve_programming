class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            while nums[i]!=i+1:
                if nums[i]!=nums[nums[i]-1]:
                    val = nums[nums[i]-1]
                    nums[nums[i]-1] = nums[i]
                    nums[i] = val
                else:
                    break
                    
        ans = []
        for i,num in enumerate(nums):
            if num!=i+1:
                ans.append(num)
        
        return ans
