#User function Template for python3

def myMax(left,right,n,arr,i):
    large = i
    if left<n and arr[left]>arr[i]:
        large = left
    if right <n and arr[large]<arr[right]:
        large = right
    
    return large

class Solution:
    #Heapify function to maintain heap property.
    def heapify(self,arr, n, i):
        # code here
        left = (i+1)*2-1
        right = (i+1)*2
        maxx = myMax(left,right,n,arr,i)
        if i!=maxx:
            arr[maxx],arr[i] = arr[i],arr[maxx]
            self.heapify(arr,n,maxx)
    
    #Function to build a Heap from array.
    def buildHeap(self,arr,n):
        # code here
        for i in range(n-1,-1,-1):
            self.heapify(arr,n,i)
        
    
    #Function to sort an array using Heap Sort.    
    def HeapSort(self, arr, n):
        #code here
        self.buildHeap(arr,n)
        for i in range(n-1,-1,-1):
            arr[0],arr[i] = arr[i],arr[0]
            self.heapify(arr,i,0)
            
            





# #User function Template for python3

# class Solution:
    
#     #Heapify function to maintain heap property.
#     def heapify(self,arr, n, i):
#         # code here
#         large = i
#         if i*2+1<n and arr[i]<arr[i*2+1]:
#             large = i*2+1
#         if i*2+2<n and arr[i]<arr[i*2+2]:
#             if large is None or arr[large]<arr[2*i+2]:
#                 large = i*2+2
#         if i!=large:
#             arr[large],arr[i]=arr[i],arr[large]
#             self.heapify(arr,n,large)
#     #Function to build a Heap from array.
#     def buildHeap(self,arr,n):
#         # code here
#         for i in range(len(arr) - 1, -1, -1):
#             self.heapify(arr, len(arr), i)
    
#     #Function to sort an array using Heap Sort.    
#     def HeapSort(self, arr, n):
#         #code here
#         self.buildHeap(arr,n)
#         for i in range(n-1,-1,-1):
#             arr[0],arr[i] = arr[i],arr[0]
#             self.heapify(arr,i,0)
