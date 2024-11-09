class Solution:
    def canCross(self, stones: List[int]) -> bool:
        @cache
        def helper(ind,prevLen):
            ans = False
            if ind == len(stones) - 1:
                return True
            for j in range(ind+1,len(stones)):
                if prevLen - 1 <= stones[j] - stones[ind] <= prevLen + 1:
                    if stones[j] - stones[ind] > prevLen + 1:
                        break
                    ans = ans or helper(j,stones[j] - stones[ind])
            return ans
        return helper(0,0)