from collections import defaultdict
import random

class RandomizedSet:

    def __init__(self):
        self.elements = defaultdict(lambda :False)
        
        

    def insert(self, val: int) -> bool:
        temp = self.elements[val]
        self.elements[val] = True
        return not temp
        

    def remove(self, val: int) -> bool:
        if val in self.elements:
            del self.elements[val]
            return True
        return False
        

    def getRandom(self) -> int:
        return list(self.elements.keys())[random.randint(0,len(self.elements.keys())-1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()