class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        values = dict.fromkeys(list(range(len(matrix), -len(matrix[0])-1, -1)), None)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if values[i-j] == None:
                    values[i-j] = matrix[i][j]
                elif values[i-j] != matrix[i][j]:
                    return False
        return True

