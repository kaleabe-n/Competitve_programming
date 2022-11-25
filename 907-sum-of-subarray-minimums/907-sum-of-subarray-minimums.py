class Solution(object):
    def sumSubarrayMins(self, arr):
        indSta = [None]
        monSta = [float('inf')]
        prefixMonSta = [None]
        i = 0
        ans = 0
        while i<len(arr):
            if arr[i]<=monSta[-1]:
                while monSta and arr[i]<=monSta[-1]:
                    monSta.pop()
                    indSta.pop()
                    prefixMonSta.pop()
                monSta.append(arr[i])
                if len(indSta)>0:
                    prefix = prefixMonSta[-1]+(i-indSta[-1])*monSta[-1]
                else:
                    prefix = (i+1)*monSta[-1]
                prefixMonSta.append(prefix)
                indSta.append(i)
            else:
                monSta.append(arr[i])
                if len(indSta)>0:
                    prefix = prefixMonSta[-1]+(i-indSta[-1])*monSta[-1]
                else:
                    prefix = (i+1)*monSTa[-1]
                prefixMonSta.append(prefix)
                indSta.append(i)
            ans+=prefixMonSta[-1]
            i+=1
        return ans%(10**9+7)
        """
        :type arr: List[int]
        :rtype: int
        """
        