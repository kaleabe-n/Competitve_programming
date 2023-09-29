class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        dp = {}
        return helper(0,stones,0,dp)

def helper(i,stones,s,dp):
    if (i,s) in dp:
        return dp[(i,s)]
    if i == len(stones)-1:
        return min(s+stones[i],s-stones[i],key=lambda x:x if x>=0 else float('inf'))
    ans1 = helper(i+1,stones,-stones[i]+s,dp)
    ans2 = helper(i+1,stones,stones[i]+s,dp)
    if ans1 < 0:
        ans1 = float('inf')
    if ans2 < 0:
        ans2 = float('inf')
    ans = min(ans1,ans2)
    dp[(i,s)] = ans
    return ans
