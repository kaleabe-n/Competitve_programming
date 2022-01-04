class Solution(object):
    def numIdenticalPairs(self, nums):
        counter=0
        for i in range(len(nums)):
            j=0
            while j<i:
                if nums[i]==nums[j]:
                    counter+=1
                j+=1
        return counter
        """
        :type nums: List[int]
        :rtype: int
        """
        
