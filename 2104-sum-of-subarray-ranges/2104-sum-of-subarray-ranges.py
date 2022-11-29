class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        indSta = [None]
        monSta = [float('inf')]
        prefixMonSta = [None]
        indSta2 = [None]
        monSta2 = [float('-inf')]
        prefixMonSta2 = [None]
        i = 0
        ans = 0
        ans2 = 0
        while i<len(nums):
            #minSum
            if nums[i]<=monSta[-1]:
                while monSta and nums[i]<=monSta[-1]:
                    monSta.pop()
                    indSta.pop()
                    prefixMonSta.pop()
                monSta.append(nums[i])
                if len(indSta)>0:
                    prefix = prefixMonSta[-1]+(i-indSta[-1])*monSta[-1]
                else:
                    prefix = (i+1)*monSta[-1]
                prefixMonSta.append(prefix)
                indSta.append(i)
            else:
                monSta.append(nums[i])
                if len(indSta)>0:
                    prefix = prefixMonSta[-1]+(i-indSta[-1])*monSta[-1]
                else:
                    prefix = (i+1)*monSta[-1]
                prefixMonSta.append(prefix)
                indSta.append(i)
            #maxsum
            if nums[i]>=monSta2[-1]:
                while monSta2 and nums[i]>=monSta2[-1]:
                    monSta2.pop()
                    indSta2.pop()
                    prefixMonSta2.pop()
                monSta2.append(nums[i])
                if len(indSta2)>0:
                    prefix = prefixMonSta2[-1]+(i-indSta2[-1])*monSta2[-1]
                else:
                    prefix = (i+1)*monSta2[-1]
                prefixMonSta2.append(prefix)
                indSta2.append(i)
            else:
                monSta2.append(nums[i])
                if len(indSta2)>0:
                    prefix = prefixMonSta2[-1]+(i-indSta2[-1])*monSta2[-1]
                else:
                    prefix = (i+1)*monSta2[-1]
                prefixMonSta2.append(prefix)
                indSta2.append(i)
            ans+=prefixMonSta[-1]
            ans2+=prefixMonSta2[-1]
            i+=1
        return ans2-ans
        """
        :type arr: List[int]
        :rtype: int
        """