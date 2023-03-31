class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        cookies.sort(reverse = True)
        buckets = [[] for i in range(k)]
        self.b = float('inf')
        def helper(cookies,buckets,i,obj):
            if i>=len(cookies):
                temp = max([sum(x) for x in buckets])
                obj.b = min(obj.b,temp)
                return temp
            tempBest = max([sum(x) for x in buckets])
            if tempBest >= obj.b:
                return tempBest
            best = float('inf')
            for ind,b in enumerate(buckets):
                newBuckets = buckets.copy()
                newBuckets[ind] = newBuckets[ind]+[cookies[i]]
                ans = helper(cookies,newBuckets,i+1,obj)
                best = min(ans,best)
            return best
        
        return helper(cookies,buckets,0,self)
