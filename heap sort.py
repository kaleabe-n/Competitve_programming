
class Solution:
    #Heapify function to maintain heap property.
    def heapify(self,arr, n, i):
        # code here
        if i >= 1 and i<n and 2*i<n and arr[i]>arr[2*i]:
            arr[i],arr[2*i] = arr[2*i],arr[i]
            self.heapify(arr,n,2*i)
        elif i >= 1 and i<n and 2*i<n and arr[i]>arr[2*i+1] and i<n:
            arr[i],arr[2*i+1] = arr[2*i+1],arr[i]
            self.heapify(arr,n,2*i)
        elif i<n and i>1 and arr[i] < arr[i//2]:
            arr[i],arr[i//2] = arr[i//2],arr[i]
            self.heapify(arr,n,i//2)
        else:
            return
    #Function to build a Heap from array.
    def buildHeap(self,arr,n):
        # code here
        arr.sort()
        arr.insert(0,None)
        for i in range(n):
            self.heapify(arr,n,i)
    
    #Function to sort an array using Heap Sort.    
    def HeapSort(self, arr, n):
        #code here
        self.buildHeap(arr,n)
        arr.pop(0)
