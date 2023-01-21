# class Solution: 
#     def select(self, arr, i):
#         # code here 
#         min = arr[i]
#         while i<len(arr):
#             if arr[i] < min:
#                 min=arr[i]
#             i+=1
#         return min
    
#     def selectionSort(self, arr,n):
#         #code here
#         for i in range(n):
#             min=self.select(arr, i)
#             arr.pop(arr.index(min,i))
#             arr.insert(i,min)


class Solution: 
    def select(self, arr, i):
        # code here 
        minInd = i
        for j in range(i,len(arr)):
            if arr[j] < arr[minInd]:
                minInd = j
        return minInd


    def selectionSort(self, arr,n):
        #code here
        for i in range(n-1):
            selected = self.select(arr,i)
            arr[i],arr[selected] = arr[selected],arr[i]
