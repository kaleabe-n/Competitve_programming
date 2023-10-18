class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        parent = [i for i in range(len(strs))]
        def find(ind):
            if parent[ind] == ind:
                return ind
            temp = find(parent[ind])
            parent[ind] = temp
            return temp
        def union(x,y):
            rootx = find(x)
            rooty = find(y)
            if rootx<rooty:
                rootx,rooty = rooty,rootx
            parent[rootx] = rooty
        for i in range(len(strs)):
            for j in range(i+1,len(strs)):
                count = 0
                for k in range(len(strs[i])):
                    if strs[i][k]!=strs[j][k]:
                        count += 1
                    if count > 2:
                        break
                if count <= 2:
                    union(i,j)
        roots = set()
        for i in range(len(strs)):
            roots.add(find(i))
        return len(roots)
