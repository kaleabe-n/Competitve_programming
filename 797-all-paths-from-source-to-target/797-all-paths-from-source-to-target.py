class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        stack = [[0,[0]]]
        ans = []
        while stack:
            curr = stack.pop()
            if curr[0] == len(graph)-1:
                ans.append(curr[1])
            else:
                for i in graph[curr[0]]:
                    stack.append([i,curr[1]+[i]])
        return ans
        