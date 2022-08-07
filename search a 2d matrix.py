class Solution(object):
    def searchMatrix(self, matrix, target):
        noOfCol = len(matrix[0])
        noOfRow = len(matrix)
        left = 1
        right = noOfRow * noOfCol
        while left<right:
            row = (((left+right)//2-1)//noOfCol)
            col = (((left+right)//2)%noOfCol)-1
            if matrix[row][col] < target:
                left = (left+right)//2+1
            else:
                right = (left+right)//2
        row = (left-1)//noOfCol
        col = left%noOfCol-1
        return matrix[row][col] == target
                
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
