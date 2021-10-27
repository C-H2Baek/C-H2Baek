# Define Class
class Car:
    color=""
    speed=0

    def __init__(self) :
        self.color = "RED"
        self.speed = 0

    def upSpeed(self, value) :
        self.speed+=value

    def downSpeed(self, value) :
        self.speed-=value


# Main Code
myCar1=Car()
myCar2=Car()

print("Car number 1 of Color is %s, Current Speed is %d KM" % (myCar1.color,myCar1.speed))


print("Car number 2 of Color is %s, Current Speed is %d KM" % (myCar2.color,myCar2.speed))
