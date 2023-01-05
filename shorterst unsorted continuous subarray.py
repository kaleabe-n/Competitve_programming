class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        monSta = []
        indSta = []
        maxx = float('-inf')
        start = float("inf")
        end = float("-inf")
        
        for ind in range(len(nums)):
            if not monSta or nums[ind] >= monSta[-1]:
                monSta.append(nums[ind])
                indSta.append(ind)
                if nums[ind] < maxx:
                    end = max(end,ind)
            else:
                while monSta and nums[ind] < monSta[-1]:
                    start = min(start,indSta.pop())
                    maxx = max(maxx,monSta.pop())
                end = max(end,ind)
                monSta.append(nums[ind])
                indSta.append(ind)
                
        return end-start+1 if end != float('-inf') else 0
