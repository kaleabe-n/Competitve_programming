class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        powers = set([1])
        temp = 1
        i = 0
        while i<24:
            temp*=2
            powers.add(temp)
            i+=1
        memo = {}
        ans = 0
        for i in deliciousness:
            for j in powers:
                if j-i in memo:
                    ans+=memo[j-i]
            if i in memo:
                memo[i]+=1
            else:
                memo[i] = 1
        return ans%(10**9+7)
        
            
        