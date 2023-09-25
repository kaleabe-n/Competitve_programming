class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        #the idea is to memoize the maximum score to continue to smaller ages which means the maximum score for younger players ot join this squad and the score if we include this one
        players = [[ages[i],scores[i]] for i in range(len(ages))]
        players.sort()
        dp = [[float('inf'),0] for _ in range(len(ages)+1)]
        maxx = 0
        for i in range(len(ages)-1,-1,-1):
            for j in range(i+1,len(ages)+1):
                   if players[i][1]<=dp[j][0] and dp[i][1]<=dp[j][1]:
                        dp[i] = [min(dp[j][0],players[i][1]),dp[j][1]]
            dp[i][1]+=players[i][1]
            maxx = max(maxx,dp[i][1])
        return maxx
    
    
