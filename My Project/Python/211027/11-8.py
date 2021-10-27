# Define Class
class Car:
    speed=0
    def upSpeed(self, value) :
        self.speed+=+value
    
        print("Cunrent Speed(Super Class) : %d" % self.speed)

class Sedan(Car) :
    def upSpeed(self, value):
        self.speed+=value

        if self.speed>150 :
            self.speed=150

        print("Cunrent Speed(Sub Class) : %d" % self.speed)

class Truck(Car):
    pass

# Define Var
sedan1, truck1=None, None

# Main Code
sedan1=Sedan()
truck1=Truck()

print("Truck-->" , end="")
truck1.upSpeed(200)
print("Sedan-->" , end="")
sedan1.upSpeed(200)