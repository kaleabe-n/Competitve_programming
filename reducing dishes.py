# class Solution:
#     def maxSatisfaction(self, satisfaction: List[int]) -> int:
#         satisfaction.sort()
#         ans = 0
#         prefix = 0
#         i = len(satisfaction)-1
#         while i>=0 and satisfaction[i]>=0:
#             prefix+=satisfaction[i]
#             ans+=prefix
#             i-=1
            
#         while i>=0:
#             prefix += satisfaction[i]
#             if prefix>=0:
#                 ans+=prefix
#             else:
#                 break
#             i-=1
#         return ans
        
        
class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        prefix = [0]
        for num in satisfaction:
            prefix.append(prefix[-1]+num)
        prefix.pop(0)
        allDishes = 0
        for i in range(len(satisfaction)):
            allDishes+=(i+1)*satisfaction[i]
        dp = [0]*len(satisfaction)
        dp[0] = allDishes
        for i in range(1,len(satisfaction)):
            dp[i] = dp[i-1]-(prefix[-1]-prefix[i-1])-satisfaction[i-1]
        ans = max(dp)
        return ans if ans>=0 else 0
            
