class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        parentAll = [i for i in range(n)]
        meetings.sort(key=lambda x:[x[2]])
        knowSecrets = set([0,firstPerson])
        parentAll[firstPerson] = 0
        sameTimeMeets = []
        currTime = meetings[0][2]
        for l,r,t in meetings:
            if t > currTime:
                tempParent = {0:0}
                for person1,person2 in sameTimeMeets:
                    if person1 in knowSecrets:
                        tempParent[person1] = 0
                    if person2 in knowSecrets:
                        tempParent[person2] = 0
                for person1,person2 in sameTimeMeets:
                    if person1 not in tempParent:
                        tempParent[person1] = person1
                    if person2 not in tempParent:
                        tempParent[person2] = person2
                    temp = union(person1,person2,tempParent)
                for person1,person2 in sameTimeMeets:
                    temp1 = find(person1,tempParent)
                    temp2 = find(person2,tempParent)
                    if temp1 == 0 or temp2 == 0:
                        knowSecrets.add(person1)
                        knowSecrets.add(person2)
                        union(person1,0,parentAll)
                        union(person2,0,parentAll)
                sameTimeMeets = [[l,r]]
                currTime = t
            elif t == currTime:
                sameTimeMeets.append([l,r])
       
        tempParent = {0:0}
        for person1,person2 in sameTimeMeets:
            if person1 in knowSecrets:
                tempParent[person1] = 0
            if person2 in knowSecrets:
                tempParent[person2] = 0
        for person1,person2 in sameTimeMeets:
            if person1 not in tempParent:
                tempParent[person1] = person1
            if person2 not in tempParent:
                tempParent[person2] = person2
            temp = union(person1,person2,tempParent)
        for person1,person2 in sameTimeMeets:
            temp1 = find(person1,tempParent)
            temp2 = find(person2,tempParent)
            if temp1 == 0 or temp2 == 0:
                knowSecrets.add(person1)
                knowSecrets.add(person2)
                union(person1,0,parentAll)
                union(person2,0,parentAll)
        return list(knowSecrets)

def find(person,parent):
    if person == parent[person]:
        return person
    temp = find(parent[person],parent)
    parent[person] = temp
    return temp
def union(x,y,parent):
    rootx = find(x,parent)
    rooty = find(y,parent)
    if rootx<rooty:
        rootx,rooty = rooty,rootx
    parent[rootx] = rooty
    return rooty
