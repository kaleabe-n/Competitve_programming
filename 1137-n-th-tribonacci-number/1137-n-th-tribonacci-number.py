class Solution:
    def tribonacci(self, n: int) -> int:
        tribs = [0,1,1]
        if n<3:
            return tribs[n]
        for i in range(3,n+1):
            if i == n:
                return sum(tribs)
            curr = sum(tribs)
            tribs.pop(0)
            tribs.append(curr)