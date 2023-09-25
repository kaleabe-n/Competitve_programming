# class Solution:
#     def minSteps(self, n: int) -> int:
#         primes = []
#         for i in range(2,n//2):
#             while n%i == 0:
#                 primes.append(i)
#                 n//=i
#         if n>1:
#             primes.append(n)
            
#         return sum(primes)



#with dp below with math above


class Solution:
    def minSteps(self, n: int) -> int:
        clip = 0
        dp = [float('inf')]*n
        dp[0] = 0
        screen = 1
        for i in range(n):
            if dp[i] == float('inf'):
                continue
            clip = i+1
            screen = i
            count = 1
            j = 1
            while True:
                screen += clip
                j+=1
                if screen>=n:
                    break
                dp[screen] = min(dp[i] + j,dp[screen])
                
        return dp[-1]
        
            
