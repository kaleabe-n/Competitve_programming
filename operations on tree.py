class LockingTree:

    def __init__(self, parent: List[int]):
        self.parent = parent
        self.child = [[] for _ in range(len(parent))]
        for i,num in enumerate(parent):
            if num == -1:
                continue
            self.child[num].append(i)
        self.locked = collections.defaultdict(lambda : False)
        

    def lock(self, num: int, user: int) -> bool:
        if not self.locked[num]:
            self.locked[num] = user
            return True
        else:
            return False
        

    def unlock(self, num: int, user: int) -> bool:
        if self.locked[num] == user:
            self.locked[num] = False
            return True
        else:
            return False
            
        

    def upgrade(self, num: int, user: int) -> bool:
        if self.locked[num]:
            return False
        temp = num
        while True:
            if self.locked[num]:
                return False
            if num == 0:
                break
            num = self.parent[num]
            
        num = temp
                
        que = collections.deque([num])
        hasLocked = False
        while que:
            curr = que.popleft()
            if self.locked[curr]:
                self.locked[curr] = False
                hasLocked = True
            for c in self.child[curr]:
                que.append(c)
        if hasLocked:
            self.locked[num] = user
            return True
        return False
        
            
        


# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)
