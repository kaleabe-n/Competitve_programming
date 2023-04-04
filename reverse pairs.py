class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        self.ans = 0
        mergeSort(nums,self)
        return self.ans
        
def mergeSort(arr,obj):
    if len(arr) == 1:
        return arr
    leftArr = arr[:len(arr)//2]
    rightArr = arr[len(arr)//2:]
    left = mergeSort(leftArr,obj)
    right = mergeSort(rightArr,obj)
    return merge(left,right,obj)

def merge(arr1,arr2,obj):
    i = len(arr2)-1
    for j in range(len(arr1)-1,-1,-1):
        num = arr1[j]
        while i>=0 and num <= 2*arr2[i]:
            i-=1
        obj.ans+=(i+1)
        
    arr2.append(float('inf'))
    arr1.append(float('inf'))
    i = 0
    j = 0
    merged = []
    while i<len(arr1) and j < len(arr2):
        if arr1[i]<=arr2[j]:
            merged.append(arr1[i])
            i+=1
        else:
            merged.append(arr2[j])
            j+=1
            
    merged.pop()
    return merged
