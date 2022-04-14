class Solution(object):
    def missingNumber(self, nums):
        nums.sort()
        counter = 0
        for i in nums:
            if i != counter:
                return counter
            counter+=1
        return len(nums)
        """
        :type nums: List[int]
        :rtype: int
        """
        
