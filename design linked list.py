class ListNode:
    def __init__(self,val,next = None):
        self.val = val
        self.next = next
        
class MyLinkedList(object):

    def __init__(self):
        self.head = None
        
    def get(self, index):
        temp = self.head
        ind = 0
        while temp is not None and ind<=index:
            if ind == index:
                return temp.val
            temp = temp.next
            ind+=1
        return -1
        """
        :type index: int
        :rtype: int
        """
        

    def addAtHead(self, val):
        newNode = ListNode(val,self.head)
        self.head = newNode
        """
        :type val: int
        :rtype: None
        """
        

    def addAtTail(self, val):
        if self.head is None:
            self.head = ListNode(val)
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = ListNode(val)
        """
        :type val: int
        :rtype: None
        """
        

    def addAtIndex(self, index, val):
        if index == 0:
            newNode = ListNode(val,self.head)
            self.head = newNode
            return
        i = 0
        prev = ListNode(None,self.head)
        temp = self.head
        while temp:
            if i == index-1:
                temp.next = ListNode(val,temp.next)
                return
            prev = prev.next
            temp = temp.next
            i+=1
        if index == i:
            prev.next = ListNode(val)
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        

    def deleteAtIndex(self, index):
        if self.head is None:
            return
        if index == 0:
            temp = self.head
            self.head = self.head.next
            temp.next = None
            return
        temp = self.head
        i = 0
        while temp is not None:
            if i == index-1:
                temp2 = temp.next
                if temp.next:
                    temp.next = temp.next.next
                    temp2.next = None
            temp = temp.next
            i+=1
        """
        :type index: int
        :rtype: None
        """
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
