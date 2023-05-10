class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        globalVisited = set()
        for c1,c2 in prerequisites:
            graph[c2].append(c1)
        
        ans = False
        for i in range(numCourses):
            # print(i)
            # if i == 40:
            #     break
            if i not in globalVisited:
                ans = ans or helper(i,graph,set(),globalVisited)
                if ans:
                    return False
                
        return True
        
        
def helper(val,graph,visited,globalVisited):
    if val in visited:
        return True
    visited.add(val)
    globalVisited.add(val)
    ans = False
    for course in graph[val]:
        ans = ans or helper(course,graph,visited,globalVisited)
    visited.remove(val)
    return ans
