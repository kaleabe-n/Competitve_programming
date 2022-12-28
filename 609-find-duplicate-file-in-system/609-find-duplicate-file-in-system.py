class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        contents = collections.defaultdict(list)
        for path in paths:
            path = path.split()
            dirr = path[0]
            for i in range(1,len(path)):
                fileName,content = path[i].split("(")
                content = content.rstrip(")")
                contents[content].append(dirr+"/"+fileName)
        ans = []
        for content in contents:
            if len(contents[content])>1:
                temp = []
                for file in contents[content]:
                    temp.append(str(file))
                ans.append(temp)
        return ans
            