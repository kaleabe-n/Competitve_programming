class Solution: 
    def select(self, arr, i):
        # code here 
        min = arr[i]
        while i<len(arr):
            if arr[i] < min:
                min=arr[i]
            i+=1
        return min
    
    def selectionSort(self, arr,n):
        #code here
        for i in range(n):
            min=self.select(arr, i)
            arr.pop(arr.index(min,i))
            arr.insert(i,min)
