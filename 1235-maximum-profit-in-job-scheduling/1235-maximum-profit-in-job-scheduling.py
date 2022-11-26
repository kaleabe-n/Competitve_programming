class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = [[startTime[i],endTime[i],profit[i]] for i in range(len(endTime))]
        jobs.sort()
        dp=[None]*len(jobs)
        dp[-1] = jobs[-1][2]
        for i in range(len(jobs)-2,-1,-1):
            j = (i+len(jobs))//2
            left = i+1
            right = len(jobs)-1
            ans=None
            while left<=right:
                j = (left+right)//2
                if jobs[j][0]>=jobs[i][1]:
                    ans=j
                    right = j-1
                    
                elif jobs[j][0]<jobs[i][1]:
                    left = j+1
            j=ans
            if j == None:
                dp[i] = max(jobs[i][2],dp[i+1])
            else:
                dp[i] = max(dp[i+1],jobs[i][2]+dp[j])
        return dp[0]
                    
                
        
        