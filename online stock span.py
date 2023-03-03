class StockSpanner:

    def __init__(self):
        self.monSta = []
        self.indSta = []
        self.ind = 0

    def next(self, price: int) -> int:
        while self.monSta and self.monSta[-1]<=price:
            self.monSta.pop()
            self.indSta.pop()
        self.ind+=1
        self.monSta.append(price)
        self.indSta.append(self.ind)
        if len(self.monSta)==1:
            return self.ind
        else:
            return self.ind-self.indSta[-2]
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
