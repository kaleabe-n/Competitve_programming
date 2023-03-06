class Solution:
    def myPow(self, x: float, n: int) -> float:
        def power(num,exp):
            if exp == 0:
                return 1
            if exp<0:
                return 1/power(num,-exp)
            if exp==1:
                return num
            else:
                if exp%2 == 0:
                    temp = power(num,exp/2)
                    return temp*temp
                else:
                    temp = power(num,exp//2)
                    return temp*temp*num
        return power(x,n)

# class Solution(object):
#     def myPow(self, x, n):
#         def power(num,exp):
#             if exp<10:
#                 return num**exp
#             else:
#                 if exp%2 == 0:
#                     return power(num,exp/2)**2
#                 else:
#                     return power(num,exp//2)**2*num
#         return power(x,n)
#         """
#         :type x: float
#         :type n: int
#         :rtype: float
#         """
        
