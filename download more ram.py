from collections import defaultdict

for i in range(int(input())):
    n,k = [int(x) for x in input().split()]
    processes = [int(x) for x in input().split()]
    reward = [int(x) for x in input().split()]
    ramIndices = defaultdict(lambda:set())
    for index,x in enumerate(processes):
        ramIndices[x].add(index)
    order = list(set(processes))
    order.sort()
    for i in order:
        if i<=k:
            for j in ramIndices[i]:
                k+=reward[j]
        else:
            break
    print(k)
        
