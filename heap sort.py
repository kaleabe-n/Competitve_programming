
#User function Template for python3

class Solution:
    
    #Heapify function to maintain heap property.
    def heapify(self,arr, n, i):
        # code here
        large = i
        if i*2+1<n and arr[i]<arr[i*2+1]:
            large = i*2+1
        if i*2+2<n and arr[i]<arr[i*2+2]:
            if large is None or arr[large]<arr[2*i+2]:
                large = i*2+2
        if i!=large:
            arr[large],arr[i]=arr[i],arr[large]
            self.heapify(arr,n,large)
    #Function to build a Heap from array.
    def buildHeap(self,arr,n):
        # code here
        for i in range(len(arr) - 1, -1, -1):
            self.heapify(arr, len(arr), i)
    
    #Function to sort an array using Heap Sort.    
    def HeapSort(self, arr, n):
        #code here
        self.buildHeap(arr,n)
        for i in range(n-1,-1,-1):
            arr[0],arr[i] = arr[i],arr[0]
            self.heapify(arr,i,0)
