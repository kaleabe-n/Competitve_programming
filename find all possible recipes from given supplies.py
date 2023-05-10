class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = collections.defaultdict(list)
        indegree = collections.defaultdict(int)
        for i,recepie in enumerate(recipes):
            for j,ing in enumerate(ingredients[i]):
                graph[ing].append(recepie)
                indegree[recepie]+=1
        
        que = collections.deque(supplies)
        ans = []
        while que:
            curr = que.popleft()
            for n in graph[curr]:
                indegree[n]-=1
                if indegree[n] == 0:
                    ans.append(n)
                    que.append(n)
        return ans
                
