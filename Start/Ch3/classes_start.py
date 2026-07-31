# LinkedIn Learning Python course by Joe Marini
# Example file for working with classes
#

class Vehicle:
  def __init__(self, bodystyle):
    self.bodystyle = bodystyle
  
  def drive(self,speed):
    self.mode = "Driving"
    self.speed = speed

class Car(Vehicle):
  def __init__(self, enginetype):
    super().__init__("Car") #inherit the vehicle class, bodystyle is "car"
    self.wheels = 4
    self.doors = 4
    self.engine = enginetype

  def drive(self,speed):
    super().drive(speed)
    print(self.mode,"my",self.engine,"car at",self.speed)

class Bike(Vehicle):
  def __init__(self, enginetype, hassidecar):
    super().__init__("Bike") #inherit the vehicle class, bodystyle is "bike"
    self.doors = 0
    if (hassidecar):
      self.wheels = 3
    else:
      self.wheels = 2
    self.engine = enginetype    
  
  def drive(self,speed):
    super().drive(speed)
    self.mode = "Riding"
    print(self.mode,"my",self.engine,"bike at",self.speed)

car1 = Car("combustion")
car2 = Car("electric")
bike1 = Bike("petrol",False)

print(f"Car 1 has {car1.wheels} wheels")
print(f"Car 2 has {car2.engine} engines")
print(f"Bike 1 has {bike1.doors} doors")

car2.drive(50)
bike1.drive(100)