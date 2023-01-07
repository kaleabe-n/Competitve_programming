class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.availables = {}
        self.availables[1] = big
        self.availables[2] = medium
        self.availables[3] = small
        

    def addCar(self, carType: int) -> bool:
        if self.availables[carType] > 0:
            self.availables[carType] -= 1
            return True
        return False


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
