from collections import defaultdict

while True:
    n = int(input())
    if n==0:
        break
    graph = defaultdict(list)
    l = int(input())
    for i in range(l):
        l,r = [int(x) for x in input().split()]
        graph[l].append(r)
        graph[r].append(l)
    visited = set()
    set1 = set()
    set2 = set()
    root = list(graph.keys())[0]
    stack = [[root,True]]
    visited.add(root)
    bicolorable = True
    while stack:
        curr,state = stack.pop()
        if state:
            set1.add(curr)
        else:
            set2.add(curr)
        for n in graph[curr]:
            if n not in visited:
                stack.append([n,not state])
                visited.add(n)
            else:
                if state and n in set1:
                    bicolorable = False
                    break
                if not state and n in set2:
                    bicolorable = False
                    break
                    
        if not bicolorable:
            break
    
    if bicolorable:
        print("BICOLOURABLE.")
    else:
        print("NOT BICOLOURABLE.")

