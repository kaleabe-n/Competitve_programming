class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        matrix.append([0] * len(matrix[0]))
        for i in range(len(matrix)-1):
            matrix[i].append(0)
            for j in range(len(matrix[i])-1):
                matrix[i][j] += matrix[i-1][j] + matrix[i][j-1] - matrix[i-1][j-1]
        self.matrix = matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans = self.matrix[row2][col2] - self.matrix[row2][col1-1] - self.matrix[row1-1][col2] + self.matrix[row1-1][col1-1]
        return ans


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

# class NumMatrix(object):

#     def __init__(self, matrix):
#         self.prefixSum = [None]*len(matrix)
#         for i in range(len(matrix)):
#             rowSum = 0
#             rowPrefixSum = [None]*len(matrix[i])
#             for j in range(len(matrix[i])):
#                 rowSum+=matrix[i][j]
#                 rowPrefixSum[j] = rowSum
#             self.prefixSum[i] = rowPrefixSum
                
                
#         """
#         :type matrix: List[List[int]]
#         """
        

#     def sumRegion(self, row1, col1, row2, col2):
#         summ = 0
#         for i in range(row1,row2+1):
#             if col1>0:
#                 summ+=self.prefixSum[i][col2]-self.prefixSum[i][col1-1]
#             else:
#                 summ+=self.prefixSum[i][col2]
#         return summ
            
#         """
#         :type row1: int
#         :type col1: int
#         :type row2: int
#         :type col2: int
#         :rtype: int
#         """
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
