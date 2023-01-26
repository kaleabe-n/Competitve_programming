class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        best = [0]*k
        for i in range(min((len(nums1)+1), k+1)):
            if k-i <= len(nums2):
                fromOne = createMaxNum(nums1,i)
                fromTwo = createMaxNum(nums2,k-i)
                currBest = combine(fromOne,fromTwo)
                best = bestOfTwoArrays(currBest,best)
        
        return best
                
        
        
def bestOfTwoArrays(arr1,arr2):
    for i in range(len(arr1)):
        if arr1[i] < arr2[i]:
            return arr2
        elif arr1[i] > arr2[i]:
            return arr1
    
    return arr1
    
    
def combine(arr1,arr2):
    i = 0
    j = 0
    combined = []
    while i<len(arr1) or j<len(arr2):
        if i >= len(arr1):
            combined.append(arr2[j])
            j+=1
        elif j>=len(arr2) or arr1[i] > arr2[j]:
            combined.append(arr1[i])
            i+=1
        elif arr1[i] == arr2[j]:
            tempi = i
            tempj = j
            while tempj < len(arr2) or tempi <  len(arr1):
                if arr1[tempi] > arr2[tempj]:
                    combined.append(arr1[i])
                    i+=1
                    break
                elif arr1[tempi] < arr2[tempj]:
                    combined.append(arr2[j])
                    j+=1
                    break
                elif tempi == len(arr1) - 1:
                    combined.append(arr2[j])
                    j+=1
                    break
                elif tempj == len(arr2) - 1:
                    combined.append(arr1[i])
                    i+=1
                    break
                tempi+=1
                tempj+=1
        else:
            combined.append(arr2[j])
            j+=1
        
    return combined

def createMaxNum(arr,k):
    toRemove = len(arr) - k
    removed = 0
    monSta = []
    for num in arr:
        while (monSta and monSta[-1] < num and removed < toRemove):
            monSta.pop()
            removed += 1
        monSta.append(num)
    
    while len(monSta) > k:
        monSta.pop()
    return monSta
