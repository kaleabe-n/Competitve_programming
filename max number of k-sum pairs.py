class Solution:
    def maxOperations(self, nums, k):
        count=0 
        keys = set(nums)
        nums = Counter(nums)
        for i in keys:
            if i*2 == k:
                count += nums[i]//2
            elif k-i in nums:
                count += max(nums[i], nums[k-i])-abs(nums[i]-nums[k-i])
                nums.pop(i)
        return count
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
