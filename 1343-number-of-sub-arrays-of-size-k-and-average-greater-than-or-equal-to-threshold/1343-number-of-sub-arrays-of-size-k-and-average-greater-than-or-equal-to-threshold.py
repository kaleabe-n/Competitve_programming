class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        leftSum = 0
        rightSum = 0
        count = 0
        for i in range(len(arr)):
            if i < k-1:
                rightSum +=arr[i]
            else: 
                if i != k-1:
                    leftSum+=arr[i-k]
                rightSum+=arr[i]
                if (rightSum-leftSum)/k>=threshold:
                    count+=1
        return count