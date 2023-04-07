from collections import defaultdict

n = int(input())
k = int(input())
graph = defaultdict(list)
for _ in range(k):
    currOp = [int(x) for x in input().split()]
    if currOp[0] == 1:
        c,u,v = currOp
        graph[v].append(u)
        graph[u].append(v)
        
    else:
        c,u = currOp
        print(*graph[u])
