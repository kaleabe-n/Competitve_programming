class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        ans = []
        indegree = defaultdict(int)
        graph = defaultdict(list)
        for l,r in adjacentPairs:
            graph[l].append(r)
            graph[r].append(l)
            indegree[l]+=1
            indegree[r]+=1
        ends = [i for i in indegree if indegree[i] == 1]
        
        for element in graph:
            if indegree[element] == 1:
                start = element
                break
        
        que = collections.deque([start])
        ans.append(start)
        while que:
            curr = que.popleft()
            for n in graph[curr]:
                indegree[n]-=1
                if indegree[n] == 1:
                    que.append(n)
                    ans.append(n)
        if ends[0] == start:
            ans.append(ends[1])
        else:
            ans.append(ends[0])
    
        return ans
                
