class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        for i,num in enumerate(nums):
            nums[i] = [num,i]
        counts = [0]*len(nums)
        mergeSort(nums,counts)
        return counts
        
        
def mergeSort(arr,counts):
    if len(arr) == 1:
        return arr
    left = mergeSort(arr[:len(arr)//2],counts)
    right = mergeSort(arr[len(arr)//2:],counts)
    merged = merge(left,right,counts)
    return merged

def merge(arr1,arr2,counts):
    i = 0
    for j in range(len(arr1)):
        num,ind = arr1[j]
        while i<len(arr2) and arr2[i][0]>=num:
            i+=1
        counts[ind] += len(arr2)-i
    arr1.append([float('-inf')])
    arr2.append([float('-inf')])
    i = 0
    j = 0
    merged = []
    while i<len(arr1) and j<len(arr2):
        if arr1[i][0]>=arr2[j][0]:
            merged.append(arr1[i])
            i+=1
        else:
            merged.append(arr2[j])
            j+=1
    merged.pop()
    return merged
            
        
