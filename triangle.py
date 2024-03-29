class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = triangle[-1]
        for i in range(len(triangle)-2,-1,-1):
            tempDp = []
            for i,num in enumerate(triangle[i]):
                tempDp.append(num+min(dp[i],dp[i+1]))
                
            dp = tempDp
            
        return dp[0]
                


# class Solution(object):
#     def minimumTotal(self, triangle):
#         dp = {}
#         for i in range(len(triangle)-1,-1,-1):
#             for j in range(len(triangle[i])):
#                 if i  == len(triangle)-1:
#                     dp[(i,j)] = triangle[i][j]
#                 else:
#                     dp[(i,j)] = triangle[i][j]+min(dp[(i+1,j)],dp[(i+1,j+1)])
#         return dp[(0,0)]
#         """
#         :type triangle: List[List[int]]
#         :rtype: int
#         """
        
