from collections import defaultdict

class Solution(object):
    def findCircleNum(self, isConnected):
        visited = defaultdict(lambda:False)
        count = 0
        for j in range(len(isConnected)):
            if not visited[j]:
                count+=1
                dfs(j,visited,isConnected)
        return count
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
def dfs(num,visited,isConnected):
    stack = [num]
    visitedDfs = defaultdict(lambda:False)
    while stack:
        temp = stack.pop()
        visitedDfs[temp] = True
        visited[temp] = True
        for i in range(len(isConnected)):
            if not visitedDfs[i] and isConnected[temp][i]==1:
                stack.append(i)
