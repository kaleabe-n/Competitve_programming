class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        graph = collections.defaultdict(list)
        indegree = [0]*len(quiet)
        for a,b in richer:
            graph[a].append(b)
            indegree[b]+=1
        que = collections.deque([i for i,x in enumerate(indegree) if x == 0])
        ans = list(range(len(quiet)))
        visited = set(que)
        while que:
            curr = que.popleft()
            minn = ans[curr]
            for n in graph[curr]:
                if n not in visited:
                    indegree[n]-=1
                    ans[n] = min(minn,ans[n],key = lambda x:quiet[x])
                    if not indegree[n]:
                        que.append(n)
                        visited.add(n)
        return ans
