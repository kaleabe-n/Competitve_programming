class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        start = 0
        end = n-2
        i = start
        ans = 0
        for j in range(n//2):
            while i <= end:
                curr = [j,i]
                second = [i,n-j-1]
                third = [second[1],n-second[0]-1]
                forth = [third[1],n-third[0]-1]
                matrix[curr[0]][curr[1]],matrix[forth[0]][forth[1]] = matrix[forth[0]][forth[1]], matrix[curr[0]][curr[1]]
                matrix[forth[0]][forth[1]],matrix[third[0]][third[1]] = matrix[third[0]][third[1]], matrix[forth[0]][forth[1]]
                matrix[third[0]][third[1]], matrix[second[0]][second[1]] = matrix[second[0]][second[1]], matrix[third[0]][third[1]]
                i+=1
            start+=1
            end-=1
            i = start

            
        """
        Do not return anything, modify matrix in-place instead.
        """
