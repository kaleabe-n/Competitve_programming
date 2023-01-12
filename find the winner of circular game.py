class Solution(object):
    def findTheWinner(self, n, k):
        def find(arr,k,curr):
                if len(arr) == 1:
                    return arr[0]
                curr = (curr + k - 1)%len(arr)
                arr.pop(curr)
                return find(arr,k,curr)
        
        return find(list(range(1,n+1)),k,0)
        """
        :type n: int
        :type k: int
        :rtype: int
        """
# class Solution:
#     def findTheWinner(self, n: int, k: int) -> int:
#         removed = set()
#         curr = -1
#         while len(removed) < n-1:
#             for i in range(k):
#                 curr += 1
#                 curr = curr % n
#                 while curr in removed:
#                     curr += 1
#                     curr = curr % n
#             removed.add(curr)
#         for i in range(n):
#             if i not in removed:
#                 return i + 1

            

            
