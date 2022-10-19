class Solution:
    def xorQueries(self, arr, queries):
        prefixXor = [None]*len(arr)
        prefixXor[0] = arr[0]
        for i in range(1,len(arr)):
            prefixXor[i] = prefixXor[i-1]^arr[i]
        ans = [None]*len(queries)
        i = 0
        for left,right in queries:
            if left == right:
                ans[i] = arr[left]
            else:
                if left == 0:
                    ans[i] = prefixXor[right]
                else:
                    ans[i] = prefixXor[right]^prefixXor[left-1]
            i+=1
        return ans
        """
        :type arr: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        