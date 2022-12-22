class Solution:
    def similarPairs(self, words: List[str]) -> int:
        count = {}
        for i in words:
            temp = str(sorted(set(i)))
            if temp in count:
                count[temp]+=1
            else:
                count[temp] = 1
        ans = 0
        memo = {0:0}
        maxx = max(count.values())
        prev = 0
        for i in range(1,maxx+1):
            memo[i] = memo[i-1] + i-1
        for i in count:
            ans+=memo[count[i]]
        return ans