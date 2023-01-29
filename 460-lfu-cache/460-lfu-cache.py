from collections import defaultdict


class LFUCache:
    def __init__(self, capacity: int):
        """time: O(1), space: O(1)"""
        self.cache = {}
        self.freqs = defaultdict(DoubleLinkedList)
        self.capacity = capacity
        self.min_freq = 0

    def get(self, key: int) -> int:
        """time: O(1), space: O(1)"""
        if key not in self.cache:
            return -1
        value = self.cache[key].value
        self.update(key, value)
        return value

    def put(self, key: int, value: int) -> None:
        """time: O(1), space: O(1)"""
        if self.capacity == 0:
            return
        if key in self.cache:
            self.update(key, value)
        else:
            if len(self.cache) == self.capacity:
                removed_key = self.freqs[self.min_freq].pop_back()
                if self.freqs[self.min_freq].is_empty:
                    del self.freqs[self.min_freq]
                del self.cache[removed_key]
            self.min_freq = 1
            self.freqs[self.min_freq].push_front(key, value, self.min_freq)
            self.cache[key] = self.freqs[self.min_freq].head

    def update(self, key: int, value: int) -> None:
        """time: O(1), space: O(1)"""
        node = self.cache[key]
        freq = node.freq
        self.freqs[freq + 1].push_front(key, value, freq + 1)
        self.cache[key] = self.freqs[freq + 1].head
        self.freqs[freq].remove_node(node)
        if (freq == self.min_freq) and self.freqs[freq].is_empty:
            self.min_freq += 1
        if self.freqs[freq].is_empty:
            del self.freqs[freq]



class DoubleNode:
    def __init__(self, key, value, freq=1, next=None, prev=None):
        self.key = key
        self.value = value
        self.freq = freq
        self.next = next
        self.prev = prev


class DoubleLinkedList:
    def __init__(self) -> None:
        """time: O(1), space: O(1)"""
        self.head = self.tail = None
        self.is_empty = True

    def __emptied__(self) -> None:
        """time: O(1), space: O(1)"""
        del self.head
        self.head = self.tail = None
        self.is_empty = True

    def push_front(self, key: int, value: int, freq: int) -> None:
        """time: O(1), space: O(1)"""
        if self.is_empty:
            self.head = self.tail = DoubleNode(key, value, freq)
            self.is_empty = False
        else:
            node = DoubleNode(key, value, freq, next=self.head)
            self.head.prev = node
            self.head = node

    def pop_front(self) -> int:
        """time: O(1), space: O(1)"""
        if self.is_empty:
            raise IndexError("LinkedList is empty!")
        key = self.head.key
        if self.head == self.tail:
            self.__emptied__()
        else:
            next = self.head.next
            self.head.next = next.prev = None
            del self.head
            self.head = next
        return key

    def pop_back(self) -> int:
        """time: O(1), space: O(1)"""
        if self.is_empty:
            raise IndexError("LinkedList is empty!")
        key = self.tail.key
        if self.head == self.tail:
            self.__emptied__()
        else:
            prev = self.tail.prev
            self.tail.prev = prev.next = None
            del self.tail
            self.tail = prev
        return key

    def remove_node(self, node: DoubleNode) -> None:
        """time: O(1), space: O(1)"""
        if self.is_empty or (node is None):
            raise IndexError("LinkedList is empty or node is None!")
        if node == self.head:
            self.pop_front()
        elif node == self.tail:
            self.pop_back()
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            node.prev = node.next = None
            del node


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)