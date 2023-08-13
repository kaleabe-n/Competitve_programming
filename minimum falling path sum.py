class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        dp = [[None for i in range(len(matrix))] for i in range(len(matrix)-1)]
        dp.append(matrix[-1])
        for i in range(len(matrix)-2,-1,-1):
            for j in range(len(matrix)-1,-1,-1):
                values = []
                if j<=len(matrix)-2:
                    values.append(dp[i+1][j+1])
                if j>0:
                    values.append(dp[i+1][j-1])
                values.append(dp[i+1][j])
                dp[i][j] = matrix[i][j] + min(values)
        return min(dp[0])
