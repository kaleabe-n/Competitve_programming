class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxx = arr[-1]
        arr[-1] = -1

        #iterate in reverse direction by keeping the maximum
        for i in range(len(arr)-2,-1,-1):
            temp = arr[i]
            arr[i] = maxx
            maxx = max(temp,maxx)
        
        return arr
        
