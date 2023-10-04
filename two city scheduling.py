class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        count = 0
        summ = 0
        costs.sort(key = lambda x:x[0]-x[1])
        for l,r in costs:
            if count<len(costs)/2:
                summ+=l
                count +=1
            else:
                summ+=r
        return summ
