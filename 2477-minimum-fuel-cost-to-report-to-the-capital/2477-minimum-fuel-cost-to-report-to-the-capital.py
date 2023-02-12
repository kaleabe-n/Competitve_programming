class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        graph = [[] for _ in range(len(roads)+1)]
        for start,end in roads:
            graph[start].append(end)
            graph[end].append(start)
        return dfs(None,0,graph,seats)[0]
def dfs(parent,child,graph,seats):
    if len(graph[child]) == 1 and graph[child][0] == parent:
        return 1,1
    if len(graph[child])== 0:
        return 0,0
    fuelTotal = 0
    totalPeople = 0
    for node in graph[child]:
        if node != parent:
            fuel,people=dfs(child,node,graph,seats)
            fuelTotal += fuel
            totalPeople += people
    if child == 0:
        return fuelTotal,totalPeople
    totalPeople+=1
    if totalPeople % seats == 0:
        fuelTotal += totalPeople // seats
    else:
        fuelTotal += totalPeople // seats + 1
    return fuelTotal,totalPeople
           