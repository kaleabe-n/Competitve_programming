class ThroneInheritance:

    def __init__(self, kingName: str):
        self.king = kingName
        self.dead = set()
        self.graph = collections.defaultdict(list)
        

    def birth(self, parentName: str, childName: str) -> None:
        self.graph[parentName].append(childName)
        

    def death(self, name: str) -> None:
        self.dead.add(name)
        

    def getInheritanceOrder(self) -> List[str]:
        stack = [self.king]
        ans = []
        while stack:
            curr = stack.pop()
            if curr not in self.dead:
                ans.append(curr)
            for n in self.graph[curr][::-1]:
                stack.append(n)
                
        return ans
            
            
        


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()
