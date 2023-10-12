# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        arr_length = mountain_arr.length()
        l = 0
        r = arr_length-1
        while l<=r:
            mid = (l+r)//2
            if mid == arr_length-1:
                mid -= 1
            if mountain_arr.get(mid)<mountain_arr.get(mid+1):
                l = mid + 1
            else:
                r = mid - 1
        peak = l
        l = 0
        r = peak
        while l<=r:
            mid = (l+r)//2
            if mountain_arr.get(mid)>target:
                r = mid - 1
            else:
                l = mid + 1
        if r>=0 and mountain_arr.get(r) == target:
            return r
        l = peak
        r = arr_length -1
        while l<=r:
            mid = (l+r)//2
            if mountain_arr.get(mid)<target:
                r = mid - 1
            else:
                l = mid + 1
        if r>=0 and mountain_arr.get(r) == target:
            return r
        return -1
                
