import math

class Solution(object):
    def smallestDivisor(self, nums, threshold):
        right = max(nums)
        left = 1
        while right>left:
            summ = 0
            mid = (left+right)//2
            for i in nums:
                summ+=math.ceil(float(i)/mid)
            if summ>threshold:
                left = (left+right)//2+1
            else:
                right = (left+right)//2
        return right
                
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        
