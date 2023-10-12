class LRUCache(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.heap = []
        self.count = collections.defaultdict(int)
        self.mapping = {}
        self.prevs = 0
        """
        :type capacity: int
        """
        

    def get(self, key):
        if key in self.mapping:
            heapq.heappush(self.heap,[self.prevs,key])
            self.prevs+=1
            self.count[key]+=1
            return self.mapping[key]
        return -1
        """
        :type key: int
        :rtype: int
        """
        

    def put(self, key, value):
        if key in self.mapping:
            heapq.heappush(self.heap,[self.prevs,key])
            self.prevs+=1
            self.count[key]+=1
            self.mapping[key] = value
            return 
        elif len(self.mapping.keys()) == self.capacity:
            _,toremove = heapq.heappop(self.heap)
            self.count[toremove]-=1
            while self.count[toremove]>0:
                _,toremove = heapq.heappop(self.heap)
                self.count[toremove]-=1
            self.mapping.pop(toremove)
        self.mapping[key] = value
        self.count[key] += 1
        heapq.heappush(self.heap,[self.prevs,key])
        self.prevs+=1
        
            
            
                
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)




# from collections import OrderedDict

# class LRUCache(object):

#     def __init__(self, capacity):
#         self.capacity = capacity
#         self.mapping = OrderedDict()
#         """
#         :type capacity: int
#         """
        

#     def get(self, key):
#         try:
#             self.mapping.move_to_end(key)
#             return self.mapping[key]
#         except:
#             return -1
#         """
#         :type key: int
#         :rtype: int
#         """
        

#     def put(self, key, value):
#         if key in self.mapping:
#             self.mapping.move_to_end(key)
#         elif len(self.mapping.keys())== self.capacity:
#             self.mapping.popitem(last = False)
#         self.mapping[key] = value
                
#         """
#         :type key: int
#         :type value: int
#         :rtype: None
#         """
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
