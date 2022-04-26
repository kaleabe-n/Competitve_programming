class Solution(object):
    def spiralOrder(self, matrix):
        lr = len(matrix[0])
        lc = len(matrix)
        lenAns = lr*lc
        ans = [None]*lenAns
        ansInd = 0
        visited = []
        i = 0
        j = 0
        dirctDict = {"right":True,"down":False,"left":False,"up":False}
        while ansInd<(lenAns):
            if (i,j) not in visited and i<lc and j<lr and i>-1 and j>-1:
                print("here")
                ans[ansInd] = matrix[i][j]
                ansInd+=1
                visited.append((i,j))
                if dirctDict["right"]:
                    j+=1
                elif dirctDict["down"]:
                    i+=1
                elif dirctDict["up"]:
                    i-=1
                elif dirctDict["left"]:
                    j-=1
                print(i,j)
            else:
                if dirctDict["right"]:
                    dirctDict["right"] = False
                    dirctDict["down"] = True
                    j-=1
                    i+=1
                elif dirctDict["down"]:
                    dirctDict["down"] = False
                    dirctDict["left"] = True
                    j-=1
                    i-=1
                elif dirctDict["left"]:
                    dirctDict["left"] = False
                    dirctDict["up"] = True
                    j+=1
                    i-=1
                elif dirctDict["up"]:
                    dirctDict["up"] = False
                    dirctDict["right"] = True
                    j+=1
                    i+=1
        return ans
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        
