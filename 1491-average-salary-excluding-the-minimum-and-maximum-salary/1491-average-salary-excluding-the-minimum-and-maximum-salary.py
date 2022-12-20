class Solution:
    def average(self, salary: List[int]) -> float:
        maxx = 0
        minn = float('inf')
        summ = 0
        for i in salary:
            summ+=i
            maxx = max(maxx,i)
            minn = min(minn,i)
        return (summ-minn-maxx)/(len(salary)-2)
        