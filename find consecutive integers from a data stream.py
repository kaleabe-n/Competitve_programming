class DataStream:
    #initialize the object with the value,k and a variable that holds the count of the last occurences of value which is initially 0
    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.count = 0
        
    #update the value of count based on the current value in the datastream and return true if the count is greater than or equal to k
    def consec(self, num: int) -> bool:
        if num == self.value:
            self.count += 1
        else:
            self.count = 0
        return self.count >= self.k
        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)
