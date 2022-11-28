class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        loses = {}
        for winner,loser in matches:
            if loser in loses:
                loses[loser]+=1
            else:
                loses[loser] = 1
            if winner not in loses:
                loses[winner] = 0
        sortedKeys = sorted(loses.keys())
        ans=[[],[]]
        for i in sortedKeys:
            if loses[i] == 0:
                ans[0].append(i)
            elif loses[i] == 1:
                ans[1].append(i)
        return ans
        