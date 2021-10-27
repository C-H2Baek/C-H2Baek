# Define Class
class Car:
    name=""
    speed=0

    def __init__(self, name, speed) :
        self.name = name
        self.speed = speed

    def getName(self) :
        return self.name

    def getSpeed(self) :
        return self.speed

# Define Var
car1, car2 = None, None

# Main Code
car1=Car("AUDI", 0)
car2=Car("BENCZ", 30)

print("Car number 1 of Color is %s, Current Speed is %d KM" % (car1.getName(),car1.getSpeed() ))
print("Car number 2 of Color is %s, Current Speed is %d KM" % (car2.getName(),car2.getSpeed() ))

