class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        indSta = []
        monSta = []
        nge = [-1]*len(nums)
        
        for i in range(2*len(nums)):
            i = i%len(nums)
            
            while monSta and monSta[-1]<nums[i]:
                ind = indSta.pop()
                nge[ind] = nums[i]
                monSta.pop()
                
            monSta.append(nums[i])
            indSta.append(i)
            
        return nge
