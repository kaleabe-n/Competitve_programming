class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prev = [1]*n
        for i in range(1,m):
            row = []
            for j in range(n):
                if j==0:
                    curr = prev[j]
                else:
                    curr = row[-1]+prev[j]
                row.append(curr)
            prev = row
            
        return prev[-1]
                    
