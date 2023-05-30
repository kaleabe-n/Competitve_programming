class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        l = nums[0]
        r = max(nums)
        while l<=r:
            temp = nums.copy()
            mid = (l+r)//2
            for i in range(len(temp)-1,0,-1):
                if temp[i]>mid:
                    temp[i-1]+=temp[i]-mid
                  
            if temp[0]<=mid:
                r = mid -1
            else:
                l = mid + 1
        
        return l
