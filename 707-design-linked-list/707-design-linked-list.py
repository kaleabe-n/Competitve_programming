class Node:
    def __init__(self,val,ne = None):
        self.val = val
        self.next = ne

class MyLinkedList:
    def __init__(self):
        self.dummy = Node(None)

    def get(self, index: int) -> int:
        i = 0
        temp = self.dummy.next
        while temp is not None:
            if i == index:
                return temp.val
            temp = temp.next
            i+=1
        return -1

    def addAtHead(self, val: int) -> None:
        newHead = Node(val,ne=self.dummy.next)
        self.dummy.next = newHead
        

    def addAtTail(self, val: int) -> None:
        temp = self.dummy
        while temp.next is not None:
            temp = temp.next
        temp.next = Node(val)
        

    def addAtIndex(self, index: int, val: int) -> None:
        i = -1
        temp = self.dummy
        while temp is not None:
            if i == index-1:
                curr = temp
                ne = temp.next
                curr.next = Node(val)
                curr.next.next = ne
            temp = temp.next
            i+=1
        

    def deleteAtIndex(self, index: int) -> None:
        i = -1
        temp = self.dummy
        while temp.next is not None:
            if i == index-1:
                ne = temp.next
                temp.next = ne.next
                ne.next = None
                return 
            temp = temp.next
            i+=1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)