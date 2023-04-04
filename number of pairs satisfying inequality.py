class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        self.soln = 0
        def mergeSort(arr):
            if len(arr) == 1:
                return arr
            left = mergeSort(arr[:len(arr)//2])
            right = mergeSort(arr[len(arr)//2:])
            ans = merge(left,right)
            
            return ans


        def merge(arr1,arr2):
            temp = []
            arr1.append(float('inf'))
            arr2.append(float('inf'))
            i,j = 0,0
            while i<len(arr1) and j<len(arr2):
                if arr1[i]>=arr2[j]:
                    temp.append(arr2[j])
                    j+=1
                else:
                    temp.append(arr1[i])
                    i+=1
            temp.pop()
            arr1.pop()
            arr2.pop()
            j = 0
            for i in range(len(arr1)):
                while j<len(arr2) and arr2[j]+diff<arr1[i]:
                    j+=1
                self.soln+=len(arr2)-j
            return temp
        for i in range(len(nums1)):
            nums1[i] -= nums2[i]
        mergeSort(nums1)
        return self.soln
            
        
