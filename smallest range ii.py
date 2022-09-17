class Solution(object):
    def smallestRangeII(self, nums, k):
        nums.sort()
        gap = nums[-1] - nums[0]
        for i in range(len(nums)-1):
            maxx = max(nums[-1]-k,nums[i]+k)
            minn = min(nums[0]+k,nums[i+1]-k)
            gap = min(gap,maxx-minn)
        return gap
            
        
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
