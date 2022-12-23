class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = [[-1,-1] for i in range(len(prices))]
        return helper(0,1,prices,memo)
        
def  helper(ind,buy,prices,memo):
    if ind>=len(prices):
        return 0
    if memo[ind][buy] != -1:
        profit = memo[ind][buy]
    elif buy:
        profit = max(-prices[ind]+helper(ind+1,0,prices,memo),helper(ind+1,1,prices,memo))
    else:
        profit = max(prices[ind]+helper(ind+1,1,prices,memo),helper(ind+1,0,prices,memo))
    memo[ind][buy] = profit
    return profit