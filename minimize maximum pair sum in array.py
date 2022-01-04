class Solution(object):
    def minPairSum(self, nums):
        nums.sort()
        middle= len(nums)//2
        temp1=nums[:middle]
        temp2=nums[middle:]
        temp2.reverse()
        print(temp2,temp1)
        maximum=temp1[0]+temp2[0]
        for i in range(middle):
            if temp1[i]+temp2[i]>maximum:
                maximum=temp1[i]+temp2[i]
        return maximum
        """
        :type nums: List[int]
        :rtype: int
        """
        
