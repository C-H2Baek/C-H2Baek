# Define Class
class Car :
    color=""
    speed=0

    def upSpeed(self,value) :
        self.speed+=value

    def downSpeed(self,value) :
        self.speed-=value

# Main Code
myCar1=Car()
myCar1.color="Red"
myCar1.speed=0

myCar2=Car()
myCar2.color="Blue"
myCar2.speed=0

myCar3=Car()
myCar3.color="Yellow"
myCar3.speed=0

myCar1.upSpeed(30)
print("Car number 1 of Color is %s, Current Speed is %d KM" % (myCar1.color,myCar1.speed))

myCar2.upSpeed(60)
print("Car number 2 of Color is %s, Current Speed is %d KM" % (myCar2.color,myCar2.speed))

myCar3.upSpeed(0)
print("Car number 3 of Color is %s, Current Speed is %d KM" % (myCar3.color,myCar3.speed))


