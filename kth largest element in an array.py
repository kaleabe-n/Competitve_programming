import random

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return helper(nums,k)
        
def helper(arr,k):
    if len(arr) == 1:
        return arr[0]
    ind = random.randint(0,len(arr)-1)
    num = arr[ind]
    left = []
    right = []
    for i in range(0,len(arr)):
        if i==ind:
            continue
        if arr[i] >= num:
            right.append(arr[i])
        else:
            left.append(arr[i])
            
    if len(right)>=k:
        return helper(right,k)
    elif len(right)+1 == k:
        return num
    else:
        return helper(left,k-len(right)-1

                      
                      
                      

# import heapq

# class Solution(object):
#     def findKthLargest(self, nums, k):
#         heap = []
#         for i in range(k):
#             heapq.heappush(heap,nums[i])
#         for i in range(k,len(nums)):
#             if nums[i]>heap[0]:
#                 heapq.heappushpop(heap,nums[i])
#         return heap[0]
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: int
#         """
        
