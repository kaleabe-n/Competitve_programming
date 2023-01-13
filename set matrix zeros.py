class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = set()
        cols = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)
        for rowNum in rows:
            for i in range(len(matrix[rowNum])):
                matrix[rowNum][i] = 0
        for colNum in cols:
            for i in range(len(matrix)):
                matrix[i][colNum] = 0
        """
        Do not return anything, modify matrix in-place instead.
        """
