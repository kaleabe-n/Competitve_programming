class Solution(object):
    def largestNumber(self, nums):
        st=""
        for i in range(len(nums)):
            nums[i]=str(nums[i])
        while len(nums)>0:
            large=nums[0]
            index=0
            for i in range(len(nums)):
                if (nums[i]+large)>(large+nums[i]):
                    large=nums[i]
                    index=i
            st+=large
            nums.pop(index)
        if st[0]=='0':
            return "0"
        return st
        """
        :type nums: List[int]
        :rtype: str
        """
        
