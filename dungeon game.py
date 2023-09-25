class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        dp = [[float(inf)]*(len(dungeon[0])+1) for _ in range(len(dungeon)+1)]
        for i in range(len(dungeon)-1,-1,-1):
            for j in range(len(dungeon[0])-1,-1,-1):
                if i == len(dungeon)-1 and j == len(dungeon[0])-1:
                    dp[i][j] = max(-(dungeon[i][j]-1),1)
                    continue
                best = min(dp[i+1][j],dp[i][j+1])
                dp[i][j] = max(1,best-dungeon[i][j])                  
                
        return dp[0][0]
