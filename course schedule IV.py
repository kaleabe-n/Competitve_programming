# class Solution:
#     def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
#         graph = [[] for _ in range(numCourses)]
#         indegree = [0]*numCourses
#         for l,r in prerequisites:
#             graph[l].append(r)
#             indegree[r]+=1
#         prereq = [set() for _ in range(numCourses)]
#         que = collections.deque([[i,[]] for i,x in enumerate(indegree) if x == 0])
#         while que:
#             curr,ancestors = que.popleft()
#             ancestors += [curr]
#             for n in graph[curr]:
#                 for anc in ancestors:
#                     prereq[n].add(anc)
#                 indegree[n]-=1
#                 if indegree[n] == 0:
#                     que.append([n,list(prereq[n])])
                    
#         ans = []
#         for l,r in queries:
#             ans.append(l in prereq[r])
#         return ans
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = collections.defaultdict(list)
        prevs = collections.defaultdict(set)
        indegree = [0]*numCourses
        for pre,after in prerequisites:
            graph[pre].append(after)
            indegree[after]+=1
        que = collections.deque([i for i in range(numCourses) if indegree[i] == 0])
        while que:
            node = que.popleft()
            for n in graph[node]:
                indegree[n]-=1
                for p in prevs[node]:
                    prevs[n].add(p)
                prevs[n].add(node)
                if indegree[n] == 0:
                    que.append(n)
        ans = []
        for pre,after in queries:
            if pre in prevs[after]:
                ans.append(True)
            else:
                ans.append((False))
            
        return ans
