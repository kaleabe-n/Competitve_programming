class Solution:
    def numTeams(self, rating: List[int]) -> int:
        dp = [None for _ in range(len(rating))]
        for i in range(len(rating)-1,-1,-1):
            less = 0
            greater = 0
            for j in range(i-1,-1,-1):
                if rating[i]>rating[j]:
                    less+=1
                else:
                    greater+=1
            dp[i] = [less,greater]
        count = 0
        for i in range(len(rating)):
            for j in range(i-1,-1,-1):
                if rating[i]<rating[j]:
                    count += dp[j][1]
                else:
                    count += dp[j][0]
        return count
        
                
