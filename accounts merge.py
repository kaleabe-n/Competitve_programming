class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = {}
        owner = {}
        groups = collections.defaultdict(list)
        ans = []
        for l in accounts:
            currOwner = l[0]
            firstElement = l[1]
            if firstElement not in parent:
                parent[firstElement] = firstElement
            owner[firstElement] = currOwner
            for i in range(2,len(l)):
                union(l[i],firstElement,parent)
                owner[l[i]] = currOwner
        for email in parent:
            groups[find(email,parent)].append(email)
        
        for group in groups:
            temp = []
            temp.append(owner[group])
            emails = groups[group]
            emails.sort()
            temp.extend(emails)
            ans.append(temp)
            
        return ans
            
        
def union(x,y,parent):
    rootx = find(x,parent)
    rooty = find(y,parent)
    if rootx==rooty:
        return
    if rootx<rooty:
        rooty,rootx = rootx,rooty
    parent[rootx] = rooty
    
def find(x,parent):
    if x not in parent:
        parent[x] = x
    if x == parent[x]:
        return x
    temp = find(parent[x],parent)
    parent[x] = temp
    return temp
        
