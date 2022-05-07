class Solution(object):
    def findUnsortedSubarray(self, nums):
        indSta = []
        numsSta = []
        start = None
        end = None
        maxx = nums[0]
        for i in range(len(nums)):
            if len(numsSta) == 0 or nums[i]>=numsSta[-1]:
                numsSta.append(nums[i])
                indSta.append(i)
                if end is not None:
                    if nums[i]<maxx:
                        end = i
            else:
                while nums[i]<numsSta[-1]:
                    temp = numsSta.pop()
                    if temp>maxx:
                        maxx = temp
                    tempInd = indSta.pop()
                    if start == None or tempInd<start:
                        start = tempInd
                    end = i
                    if len(numsSta) == 0:
                        break
        return end-start+1 if end is not None else 0
            
        """
        :type nums: List[int]
        :rtype: int
        """
        
