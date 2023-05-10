class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = set()
        indegree = defaultdict(int)
        graph = collections.defaultdict(list)
        for l,r in prerequisites:
            indegree[l]+=1
            graph[r].append(l)
        for i in range(numCourses):
            if i not in visited and indegree[i] == 0:
                stack = [i]
                visited.add(i)
                while stack:
                    curr = stack.pop()
                    for n in graph[curr]:
                        if n not in visited:
                            indegree[n]-=1
                            if indegree[n] == 0:
                                stack.append(n)
                                visited.add(n)
                                
        return max(indegree.values())==0
