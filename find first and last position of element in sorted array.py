class Solution(object):
    def searchRange(self, nums, target):
        left = 0
        right = len(nums)-1
        rightEnd = None
        while right>left:
            if nums[(right+left)//2]<=target:
                if nums[(right+left)//2+1]>target:
                    rightEnd = (right+left)//2
                    break
                else:
                    left = (right+left)//2+1
            else:
                right = (right+left)//2
        if right == left and rightEnd == None:
            rightEnd = left
        rightEnd = len(nums)-1 if rightEnd == None else rightEnd
        left = 0
        right = rightEnd if rightEnd is not None else len(nums)-1
        leftEnd = None
        while right>left:
            if nums[(right+left)//2]<target:
                if nums[(right+left)//2+1]==target:
                    leftEnd = (right+left)//2+1
                    break
                else:
                    left = (right+left)//2+1
            else:
                right = (right+left)//2
        if right == left and leftEnd == None:
            leftEnd = left
        leftEnd = 0 if leftEnd == None else leftEnd
        if len(nums)>0 and nums[rightEnd] == target:
            return [leftEnd,rightEnd]
        return [-1,-1]
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """        
