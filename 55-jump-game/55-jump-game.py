class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = 0
        maxReachable = i+nums[0]
        while i<=maxReachable and i < len(nums):
            if i == len(nums)-1:
                return True
            maxReachable = max(maxReachable,i+nums[i])
            i+=1
        
        return False
                
        
        