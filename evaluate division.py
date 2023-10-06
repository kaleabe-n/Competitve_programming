class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = collections.defaultdict(lambda :collections.defaultdict(lambda :float('inf')))
        variables = set()
        for i in range(len(equations)):
            l,r = equations[i]
            graph[l][r] = values[i]
            graph[r][l] = 1/values[i]
            variables.add(l)
            variables.add(r)
        for var in variables:
            for l in variables:
                if l == var:
                    continue
                for r in variables:
                    if r == var:
                        continue
                    graph[l][r] = min(graph[l][r],graph[l][var]*graph[var][r])
        ans = []
        for l,r in queries:
            if l not in variables or r not in variables:
                ans.append(-1.0)
            else:
                if graph[l][r] != float('inf'):
                    ans.append(graph[l][r])
                else:
                    ans.append(-1)
        return ans
        
