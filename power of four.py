# class Solution:
#     def isPowerOfFour(self, n: int) -> bool:
#         if n<1:
#             return False
#         if n==1:
#             return True
#         if n%4!=0:
#             return False  78
#         return self.isPowerOfFour(n//4)

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        num=1
        def helper(n,num):
            if num>n:
                return False
            if num == n:
                return True
            return helper(n,num*4)
        return helper(n,num)
    
# class Solution:
#     def isPowerOfFour(self, n: int) -> bool:
#         if n<1:
#             return False
#         if n==1:
#             return True
#         return self.isPowerOfFour(n/4)


# class Solution(object):
#     def isPowerOfFour(self, n):
#         if n>1:
#             return self.isPowerOfFour(n/4.0)
#         elif n==1:
#             return True
#         else:
#             return False
#         """
#         :type n: int
#         :rtype: bool
#         """
        
