class Solution(object):
    def productExceptSelf(self, nums):
        products = [1]*len(nums)
        pro = 1
        for i in range(1,len(nums)):
            pro*=nums[i-1]
            products[i] = pro
        pro = 1
        for i in range(len(nums)-2,-1,-1):
            pro*=nums[i+1]
            products[i]*=pro
        return products
    
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
