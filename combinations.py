class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        options = [[]]
        for i in range(1,n+1):
            temp = []
            for op in options:
                if len(op)+1<k:
                    temp.append(op+[i])
                elif len(op)+1 == k:
                    ans.append(op+[i])
            options.extend(temp)
        return ans
