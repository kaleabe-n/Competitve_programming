class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        prefixSum = [nums[0]]
        ans = [None]*len(queries)
        for i in range(1,len(nums)):
            prefixSum.append(prefixSum[-1]+nums[i])
        for i in range(len(queries)):
            l = 0
            r = len(nums)-1
            if prefixSum[0]>queries[i]:
                ans[i] = 0
                continue
            while l < r:
                mid = (l+r)//2
                if prefixSum[mid] < queries[i]:
                    l = mid+1
                elif prefixSum[mid] > queries[i]:
                    r = mid-1
                else:
                    ans[i] = mid+1
                    break
            if ans[i] == None:
                ans[i] = r+1 if queries[i]>=prefixSum[r] else r
        return ans