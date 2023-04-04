n,k = [int(x) for x in input().split()]
players = [[[int(x),i]] for i,x in enumerate(input().split())]
 
def recur(players):
    if len(players) == 1:
        return players[0]
    newPlayers = []
    for i in range(0,len(players),2):
        temp1 = []
        temp2 = []
        for p in players[i]:
            if p[0] >= players[i+1][0][0]-k:
                temp1.append(p)
        for p in players[i+1]:
            if p[0] >= players[i][0][0]-k:
                temp2.append(p)
        temp1.append([float('inf')])
        temp2.append([float('inf')])
        temp = []
        i = 0
        j = 0
        while i<len(temp1) and j<len(temp2):
            if temp1[i][0]<=temp2[j][0]:
                temp.append(temp1[i])
                i+=1
            else:
                temp.append(temp2[j])
                j+=1
                
        temp.pop()
        newPlayers.append(temp)
        
    return recur(newPlayers)
    
ans = recur(players)
ans.sort(key=lambda x:x[1])
print(*[x[1]+1 for x in ans])
