class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        memo = [[-1,-1] for i in range(len(prices))]
        return helper(0,1,prices,memo,fee)
        
def  helper(ind,buy,prices,memo,fee):
    if ind>=len(prices):
        return 0
    if memo[ind][buy] != -1:
        profit = memo[ind][buy]
    elif buy:
        profit = max(-fee-prices[ind]+helper(ind+1,0,prices,memo,fee),helper(ind+1,1,prices,memo,fee))
    else:
        profit = max(prices[ind]+helper(ind+1,1,prices,memo,fee),helper(ind+1,0,prices,memo,fee))
    memo[ind][buy] = profit
    return profit
