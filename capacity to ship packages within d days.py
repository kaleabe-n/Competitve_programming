def isAble(weights,days,capacity):
    i = 0
    while days>0:
        temp = capacity
        while temp>0 and i<len(weights):
            temp-=weights[i]
            i+=1
        if temp<0:
            i-=1
        days-=1
    return i==len(weights)
    
class Solution(object):
    def shipWithinDays(self, weights, days):
        left = 1
        right = sum(weights)
        while left<right:
            if not isAble(weights,days,(left+right)//2):
                if isAble(weights,days,(left+right)//2+1):
                    return (left+right)//2+1
                else:
                    left = (left+right)//2+1
            else:
                right = (left+right)//2
        return left
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
