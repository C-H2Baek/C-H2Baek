# Define Class
class Car:
    color=""
    speed=0

    def __init__(self, value1, value2) :
        self.color = value1
        self.speed = value2

    def upSpeed(self, value) :
        self.speed+=value

    def downSpeed(self, value) :
        self.speed-=value


# Main Code
myCar1=Car("RED", 30)
myCar2=Car("BLUE", 60)

print("Car number 1 of Color is %s, Current Speed is %d KM" % (myCar1.color,myCar1.speed))


print("Car number 2 of Color is %s, Current Speed is %d KM" % (myCar2.color,myCar2.speed))
