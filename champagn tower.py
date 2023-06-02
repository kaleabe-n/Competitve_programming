class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [[poured]]
        for i in range(query_row):
            currDp = []
            for j in range(i+2):
                if j==0:
                    currDp.append(max(0,dp[-1][0]-1)/2)
                elif j==i+1:
                    currDp.append(max(0,dp[-1][-1]-1)/2)
                else:
                    currDp.append((max(dp[-1][j-1]-1,0)+max(0,dp[-1][j]-1))/2)
            dp.append(currDp)
        return dp[query_row][query_glass] if dp[query_row][query_glass]<=1 else 1
                
        
