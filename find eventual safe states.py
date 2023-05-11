class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        reverseGraph = [[]for _ in range(len(graph))]
        indegree = [0]*len(graph)
        for i in range(len(graph)):
            for j in graph[i]:
                reverseGraph[j].append(i)
                indegree[i]+=1
        terminals = [i for i,x in enumerate(indegree) if x == 0]
        tSet = set(terminals)
        que = deque(terminals)
        ans = []
        visited = set(que)
        while que:
            curr = que.popleft()
            ans.append(curr)
            for n in reverseGraph[curr]:
                if n not in visited:
                    indegree[n]-=1
                    if indegree[n] == 0:
                        que.append(n)
                        visited.add(n)
        ans.sort()
        return ans
