# Define Class
class Car:
    speed=0

    def upSpeed(self, value) :
        self.speed=self.speed+value
    
    def downSpeed(self,value) :
        self.speed=self.speed-value

class Sedan(Car) :
    seatNum =0

    def getSeatNum(self):
        return self.seatNum

class Truck(Car):
    capacity=0

    def getCapacity(self) :
        return self.capacity

# Define Var
sedan1, truck1=None, None

# Main Code
sedan1=Sedan()
truck1=Truck()

sedan1.upSpeed(100)
truck1.upSpeed(80)

sedan1.seatNum=5
truck1.capacity=50

print("Sedan Speed %d KM, Seat %d EA." %(sedan1.speed,sedan1.getSeatNum() ))
print("Truck Speed %d KM, Capacity %d T." %(truck1.speed,truck1.getCapacity() ))