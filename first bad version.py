# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n
        while left<=right:
            mid = (left+right)//2
            if isBadVersion(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left



# # The isBadVersion API is already defined for you.
# # @param version, an integer
# # @return a bool
# # def isBadVersion(version):

# class Solution(object):
#     def firstBadVersion(self, n):
#         left = 1
#         right = n
#         while right-left>0:
#             if not isBadVersion((left+right)//2):
#                 if isBadVersion((left+right)//2+1):
#                     return (left+right)//2+1
#                 else:
#                     left = (left+right)//2+1
#             else:
#                 right = (left+right)//2
#         return left
#         """
#         :type n: int
#         :rtype: int
#         """
        
