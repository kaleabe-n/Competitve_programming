class Solution(object):
    def minIncrementForUnique(self, nums):
        nums.sort()
        i = 0
        inc = 0
        while i<(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i+1]+=1
                inc+=1
            elif (nums[i] > nums[i+1]):
                temp = (nums[i]-nums[i+1]+1)
                nums[i+1]+= temp
                inc+=temp
            i+=1
        return inc
        """
        :type nums: List[int]
        :rtype: int
        """
        
