class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l = 0
        r = len(arr)-1
        while l<=r:
            mid = (l+r)//2
            if mid == 0:
                mid = 1
            if arr[mid]<arr[mid-1]:
                r = mid-1
            else:
                l = mid+1
                
        return r
