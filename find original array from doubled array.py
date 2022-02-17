class Solution(object):
    def findOriginalArray(self, changed):
        changed.sort()
        originalLength = len(changed)//2
        i = 0
        j = 1
        while len(changed) > originalLength:
            if j>=len(changed):
                return []
            elif changed[i]*2 == changed[j] and i != j:
                changed.pop(j)
                i+=1
            else:
                j+=1
        if(len(changed) == originalLength):
            return changed
        else:
            return []
        """
        :type changed: List[int]
        :rtype: List[int]
        """
        
