class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        indSum = 0
        maxIndSum = len(mat) - 1 + len(mat[0]) - 1
        i = 0
        state = "u"
        ans = []
        while indSum<=maxIndSum:
            if state == "u":
                while True:
                    if 0<=i<len(mat) and 0<=indSum-i<len(mat[0]):
                        ans.append(mat[i][indSum-i])
                    if i == 0 or indSum-i == len(mat[0]):
                        state = "d"
                        indSum+=1
                        break
                    i-=1
            elif state == "d":
                while True:
                    if 0<=i<len(mat) and 0<=indSum-i<len(mat[0]):
                        ans.append(mat[i][indSum-i])
                    if indSum-i == 0 or i == len(mat):
                        state = "u"
                        i+=1
                        indSum+=1
                        break
                    i+=1
        return ans
            