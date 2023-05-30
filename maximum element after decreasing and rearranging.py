class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        arr[0] = 1
        maxx = 1
        prev = 1
        for i in range(1,len(arr)):
            if arr[i]>1+prev:
                arr[i] = 1+prev
            maxx = max(maxx,arr[i])
            prev = arr[i]
            
        return maxx
