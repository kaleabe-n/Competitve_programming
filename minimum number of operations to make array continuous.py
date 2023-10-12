class Solution:
    def minOperations(self, nums: List[int]) -> int:
        uniques = list(set(nums))
        uniques.sort()
        minn = float('inf')
        for i in range(len(uniques)):
            curr = uniques[i]
            end = curr + len(nums) - 1
            l = i
            r = len(uniques)-1
            while l<=r:
                mid = (l+r)//2
                if uniques[mid]<=end:
                    l = mid + 1
                else:
                    r = mid - 1
            
            minn = min(minn,len(nums)-(r-i+1))
        return minn
