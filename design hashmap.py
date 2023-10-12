class ListNode:
    def __init__(self,key,val,ne=None):
        self.key = key
        self.val = val
        self.next = ne

class MyHashMap:

    def __init__(self):
        self.arr = [None]*1024

    def put(self, key: int, value: int) -> None:
        currInd = key%1024
        if self.arr[currInd] == None:
            self.arr[currInd] = ListNode(key,value)
            return
        temp = self.arr[currInd]
        while temp:
            if temp.key == key:
                temp.val  = value
                return
            if not temp.next:
                temp.next = ListNode(key,value)
            temp = temp.next
            
        
    def get(self, key: int) -> int:
        currInd = key%1024
        if self.arr[currInd] == None:
            return -1
        temp = self.arr[currInd]
        while temp:
            if temp.key == key:
                return temp.val
            temp = temp.next
        return -1
        

    def remove(self, key: int) -> None:
        currInd = key%1024
        if self.arr[currInd] == None:
            return 
        if self.arr[currInd].key == key:
            temp = self.arr[currInd]
            self.arr[currInd] = self.arr[currInd].next
            temp.next = None
            return 
        temp = self.arr[currInd]
        while temp and temp.next:
            if temp.next.key == key:
                t = temp.next
                temp.next = temp.next.next
                t.next = None
                return
            temp = temp.next
            
        
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
