# Define Class
class Car:
    color=""
    speed=0
    count=0

    def __init__(self) :
        self.speed = 0
        Car.count += 1

# Define Var
myCar1, myCar2 = None, None

# Main Code
myCar1=Car()
myCar1.speed=30
print("Car 1 Speed is %d, COunt is %d EA" % (myCar1.speed,Car.count ))

myCar2=Car()
myCar2.speed=30
print("Car 2 Speed is %d, COunt is %d EA" % (myCar2.speed,Car.count ))
