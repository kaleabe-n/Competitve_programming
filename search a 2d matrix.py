class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        #time complexiy o(m+n) space complexity o(1)
        
        
        row = 0
        #search for the row vertically
        for i in range(-1,len(matrix)-1):
            if matrix[i+1][0] > target:
                row = i
                break
        else:
            row = len(matrix) - 1

        #search for the number within ther row
        for num in matrix[row]:
            if num == target:
                return True
        
        return False

