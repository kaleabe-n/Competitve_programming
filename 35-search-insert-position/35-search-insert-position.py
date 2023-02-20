class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)
        while l<r:
            mid = (r+l)//2
            if target < nums[mid]:
                r = mid
            elif target > nums[mid]:
                l = mid+1
            else:
                return mid
        return l
        